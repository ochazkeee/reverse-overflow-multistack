// multiple_stack.c
#include "multiple_stack.h"
#include <stdio.h>

void init_multi_stack(MultiStack* ms, int num_stacks) {
    ms->num_stacks = num_stacks;
    int chunk = STACK_SIZE / num_stacks;
    int leftover = STACK_SIZE % num_stacks;  // 남는 공간 처리
    for (int i = 0; i < num_stacks; i++) {
        ms->base[i] = i * chunk;
        ms->top[i] = ms->base[i] - 1;
        ms->limit[i] = (i + 1) * chunk - 1 + (i == num_stacks - 1 ? leftover : 0);  // 마지막 스택에 남은 공간 추가
    }
}

bool push(MultiStack* ms, int stack_id, int value) {
    if (stack_id < 0 || stack_id >= ms->num_stacks) return false;

    // 스택 공간에 여유가 있으면 그곳에 삽입
    if (ms->top[stack_id] < ms->limit[stack_id]) {
        ms->top[stack_id]++;
        ms->data[ms->top[stack_id]] = value;
        return true;
    }

    // Reverse overflow 전략
    for (int offset = 1; offset < ms->num_stacks; offset++) {
        int other_id = (stack_id + offset) % ms->num_stacks;
        if (ms->top[other_id] < ms->limit[other_id]) {
            ms->top[other_id]++;
            ms->data[ms->top[other_id]] = value;
            printf("[INFO] Stack %d overflowed. Stored value (%d) in stack %d at index %d\n",
                stack_id, value, other_id, ms->top[other_id]);
            return true;
        }
    }

    // 모든 스택이 꽉 찼을 때
    printf("[ERROR] All stacks are full. Cannot push %d\n", value);
    return false;
}

bool pop(MultiStack* ms, int stack_id, int* out) {
    if (stack_id < 0 || stack_id >= ms->num_stacks) return false;

    // 스택이 비어 있으면 팝할 수 없음
    if (ms->top[stack_id] < ms->base[stack_id]) return false;

    *out = ms->data[ms->top[stack_id]];
    ms->top[stack_id]--;
    return true;
}

void print_stack(MultiStack* ms, int stack_id) {
    if (stack_id < 0 || stack_id >= ms->num_stacks) return;

    printf("Stack %d: ", stack_id);
    for (int i = ms->base[stack_id]; i <= ms->top[stack_id]; i++) {
        printf("%d ", ms->data[i]);
    }
    printf("\n");
}
