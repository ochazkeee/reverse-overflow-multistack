import time
import random

ARRAY_SIZE = 10000
NUM_STACKS = 20
PUSH_RATIO = [0.9, 0.05, 0.05]
POP_PROB = 0.3  # pop이 일어날 확률

# Refactor 방식 (pop 포함)
class RefactorStackFixed:
    def __init__(self, size, k):
        self.k = k
        self.size = size
        self.arr = [None] * size
        self.part_size = size // k
        self.starts = [i * self.part_size for i in range(k)]
        self.ends = [(i + 1) * self.part_size - 1 for i in range(k)]
        self.tops = [start - 1 for start in self.starts]

    def _refactor(self, stack_id):
        sid = stack_id + 1
        while sid < self.k:
            for i in range(self.ends[sid], self.starts[sid], -1):
                if self.arr[i] is None and self.arr[i - 1] is not None:
                    self.arr[i] = self.arr[i - 1]
                    self.arr[i - 1] = None
                    if self.tops[sid] == i - 1:
                        self.tops[sid] = i
            sid += 1

    def push(self, stack_id, value):
        next_pos = self.tops[stack_id] + 1
        if next_pos <= self.ends[stack_id] and self.arr[next_pos] is None:
            self.tops[stack_id] = next_pos
            self.arr[next_pos] = value
            return True

        self._refactor(stack_id)

        next_pos = self.tops[stack_id] + 1
        if next_pos <= self.ends[stack_id] and self.arr[next_pos] is None:
            self.tops[stack_id] = next_pos
            self.arr[next_pos] = value
            return True

        return False

    def pop(self, stack_id):
        if self.tops[stack_id] >= self.starts[stack_id]:
            val = self.arr[self.tops[stack_id]]
            self.arr[self.tops[stack_id]] = None
            self.tops[stack_id] -= 1
            return val
        return None
    def pop(self, stack_id):
        if self.tops[stack_id] >= self.starts[stack_id]:
            val = self.arr[self.tops[stack_id]]
            self.arr[self.tops[stack_id]] = None
            self.tops[stack_id] -= 1
            return val
        return None


# Reverse Overflow 방식 (pop 포함)
class ReverseOverflowStack:
    def __init__(self, size, k):
        self.array = [None] * size         # 실제 데이터 저장
        self.owner = [None] * size         # 해당 인덱스를 사용하는 스택 번호
        self.tops = [-1] * k               # 각 스택의 top 인덱스 추적
        self.size = size
        self.k = k
        self.free_indices = list(range(size - 1, -1, -1))  # 빈 인덱스 관리 (stack처럼 사용)

    def push(self, stack_id, value):
        if not self.free_indices:
            return False  # 공간 없음
        i = self.free_indices.pop()  # 가장 최근의 빈 공간을 사용
        self.array[i] = value
        self.owner[i] = stack_id
        self.tops[stack_id] = max(self.tops[stack_id], i)
        return True

    def pop(self, stack_id):
        for i in range(self.tops[stack_id], -1, -1):
            if self.owner[i] == stack_id and self.array[i] is not None:
                self.array[i] = None
                self.owner[i] = None
                self.tops[stack_id] = i - 1
                self.free_indices.append(i)  # 공간 회수
                return True
        return False

#최적화된 Refactor 방식
class SmartRefactorStack:
    def __init__(self, size, k):
        self.k = k
        self.size = size
        self.arr = [None] * size
        self.part_size = size // k
        self.starts = [i * self.part_size for i in range(k)]
        self.ends = [(i + 1) * self.part_size - 1 for i in range(k)]
        self.tops = [start - 1 for start in self.starts]

    def _refactor(self, stack_id):
        for sid in range(self.k - 1, stack_id, -1):
            for i in reversed(range(self.starts[sid], self.ends[sid])):
                if self.arr[i] is not None and self.arr[i + 1] is None:
                    self.arr[i + 1] = self.arr[i]
                    self.arr[i] = None
                    if self.tops[sid] == i:
                        self.tops[sid] = i + 1

    def push(self, stack_id, value):
        next_pos = self.tops[stack_id] + 1
        if next_pos <= self.ends[stack_id] and self.arr[next_pos] is None:
            self.tops[stack_id] = next_pos
            self.arr[next_pos] = value
            return True

        self._refactor(stack_id)

        next_pos = self.tops[stack_id] + 1
        if next_pos <= self.ends[stack_id] and self.arr[next_pos] is None:
            self.tops[stack_id] = next_pos
            self.arr[next_pos] = value
            return True

        return False

    def pop(self, stack_id):
        if self.tops[stack_id] >= self.starts[stack_id]:
            val = self.arr[self.tops[stack_id]]
            self.arr[self.tops[stack_id]] = None
            self.tops[stack_id] -= 1
            return val
        return None

#knuth 방식
class KnuthLinkedStack:
    def __init__(self, size, k):
        self.size = size
        self.k = k
        self.nodes = [{'val': None, 'next': None} for _ in range(size)]
        self.tops = [None] * k
        self.free = list(range(size))  # free list 관리

    def push(self, stack_id, value):
        if not self.free:
            return False  # 공간 없음

        idx = self.free.pop()  # free에서 하나 꺼냄
        self.nodes[idx]['val'] = value
        self.nodes[idx]['next'] = self.tops[stack_id]  # 기존 top을 연결
        self.tops[stack_id] = idx  # 새로운 top 갱신
        return True

    def pop(self, stack_id):
        top_idx = self.tops[stack_id]
        if top_idx is None:
            return False  # 빈 스택

        self.tops[stack_id] = self.nodes[top_idx]['next']  # top 이동
        self.nodes[top_idx] = {'val': None, 'next': None}  # 초기화
        self.free.append(top_idx)  # free list로 반환
        return True
