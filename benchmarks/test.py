import time
import random
import platform
import matplotlib.pyplot as plt
import sys
from Implementations import (
    RefactorStackFixed,
    SmartRefactorStack,
    ReverseOverflowStack,
    KnuthLinkedStack
)

# 전략 정의
strategies = {
    "Refactor 방식": RefactorStackFixed,
    "최적화된 Refactor 방식": SmartRefactorStack,
    "Reverse Overflow 방식": ReverseOverflowStack,
    "Knuth Linked Stack": KnuthLinkedStack
}

# 메모리 측정 함수
def get_deep_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_deep_size(v, seen) + get_deep_size(k, seen) for k, v in obj.items()])
    elif hasattr(obj, '__dict__'):
        size += get_deep_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_deep_size(i, seen) for i in obj])
    return size

# 단일 실험 수행
def run_experiment(ManagerClass, array_size, num_stacks, push_ratios, pop_prob, iterations=10000):
    stack = ManagerClass(array_size, num_stacks)
    success_push, success_pop = 0, 0
    start = time.time()

    for _ in range(iterations):
        op = "push" if random.random() > pop_prob else "pop"
        target_stack = random.choices(range(num_stacks), weights=push_ratios, k=1)[0]
        if op == "push":
            if stack.push(target_stack, random.randint(1, 100)):
                success_push += 1
        else:
            if stack.pop(target_stack):
                success_pop += 1

    elapsed = time.time() - start
    memory_used = get_deep_size(stack)
    return success_push, success_pop, elapsed, memory_used

# 여러 번 반복해서 평균치 측정
def repeat_experiments(array_size, num_stacks, push_ratios, pop_prob, iterations=10000, repeat=5):
    summary = {}
    for label, ManagerClass in strategies.items():
        total_push = total_pop = total_time = total_mem = 0.0
        for _ in range(repeat):
            sp, pp, t, m = run_experiment(ManagerClass, array_size, num_stacks, push_ratios, pop_prob, iterations)
            total_push += sp
            total_pop += pp
            total_time += t
            total_mem += m
        summary[label] = {
            "avg_push": total_push / repeat,
            "avg_pop": total_pop / repeat,
            "avg_time": total_time / repeat,
            "avg_memory": total_mem / repeat
        }
    return summary

# 시각화 개선 버전
def visualize_results(summary):
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':
        plt.rc('font', family='AppleGothic')
    else:
        plt.rc('font', family='NanumGothic')
    plt.rcParams['axes.unicode_minus'] = False

    labels = list(summary.keys())
    push_vals = [summary[label]["avg_push"] for label in labels]
    pop_vals = [summary[label]["avg_pop"] for label in labels]
    time_vals = [summary[label]["avg_time"] for label in labels]
    mem_vals = [summary[label]["avg_memory"] / 1024 for label in labels]  # KB로 변환
    x = range(len(labels))
    width = 0.6
    colors = ['#4CAF50', '#2196F3', '#FFC107', '#E91E63']

    plt.figure(figsize=(20, 5))

    def add_labels(values, fmt="%.0f"):
        for i, v in enumerate(values):
            plt.text(i, v + max(values) * 0.02, fmt % v, ha='center', fontsize=9)

    plt.subplot(1, 4, 1)
    plt.bar(x, push_vals, color=colors)
    plt.title("평균 Push 성공 횟수")
    plt.xticks(x, labels, rotation=15)
    add_labels(push_vals)

    plt.subplot(1, 4, 2)
    plt.bar(x, pop_vals, color=colors)
    plt.title("평균 Pop 성공 횟수")
    plt.xticks(x, labels, rotation=15)
    add_labels(pop_vals)

    plt.subplot(1, 4, 3)
    plt.bar(x, time_vals, color=colors)
    plt.title("평균 실행 시간 (초)")
    plt.xticks(x, labels, rotation=15)
    add_labels(time_vals, fmt="%.3f")

    plt.subplot(1, 4, 4)
    plt.bar(x, mem_vals, color=colors)
    plt.title("평균 메모리 사용량 (KB)")
    plt.xticks(x, labels, rotation=15)
    add_labels(mem_vals, fmt="%.1f")

    plt.tight_layout()
    plt.show()

# 실험 조건들
experiments = [
    # 균등 분산, 소형 스택, 낮은 pop 확률
    {"PUSH_RATIO": [0.2] * 5, "NUM_STACKS": 5, "POP_PROB": 0.1, "array_size": 2000},

    # 1개 스택 집중형, 대형 스택 구조, 중간 pop 확률
    {"PUSH_RATIO": [0.95] + [0.0025] * 20, "NUM_STACKS": 21, "POP_PROB": 0.5, "array_size": 10000},

    # 절반에만 분산된 구조, 중형 스택, 높은 pop 확률
    {"PUSH_RATIO": [0.5] * 2 + [0.0] * 8, "NUM_STACKS": 10, "POP_PROB": 0.8, "array_size": 5000},

    # 완전 균등, 대형 스택, 중간 pop 확률
    {"PUSH_RATIO": [1/50] * 50, "NUM_STACKS": 50, "POP_PROB": 0.5, "array_size": 20000},

    # 가운데 집중형, 중형 스택, 낮은 pop 확률
    {"PUSH_RATIO": [0.05]*5 + [0.5] + [0.05]*5, "NUM_STACKS": 11, "POP_PROB": 0.2, "array_size": 10000}
]


# 실행
for exp in experiments:
    print(f"\n 실험 조건: PUSH_RATIO={exp['PUSH_RATIO']}, NUM_STACKS={exp['NUM_STACKS']}, POP_PROB={exp['POP_PROB']}")
    summary = repeat_experiments(
        array_size=exp["array_size"],
        num_stacks=exp["NUM_STACKS"],
        push_ratios=exp["PUSH_RATIO"],
        pop_prob=exp["POP_PROB"],
        iterations=10000,
        repeat=5
    )
    for label, metrics in summary.items():
        print(f"{label}: 평균 Push={metrics['avg_push']:.1f}, 평균 Pop={metrics['avg_pop']:.1f}, 평균 시간={metrics['avg_time']:.4f}s, 평균 메모리={metrics['avg_memory'] / 1024:.1f}KB")
    visualize_results(summary)