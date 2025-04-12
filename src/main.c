// main.c
#include "multiple_stack.h"
#include <stdio.h>

int main() {
    MultiStack ms;
    init_multi_stack(&ms, MAX_STACKS);

    push(&ms, 0, 10);
    push(&ms, 0, 20);
    push(&ms, 1, 30);
    push(&ms, 2, 40);

    print_stack(&ms, 0);
    print_stack(&ms, 1);
    print_stack(&ms, 2);

    int val;
    if (pop(&ms, 0, &val)) {
        printf("Popped from stack 0: %d\n", val);
    }

    print_stack(&ms, 0);
    return 0;
}
