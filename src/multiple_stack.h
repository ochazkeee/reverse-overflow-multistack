// multiple_stack.h
#ifndef MULTIPLE_STACK_H
#define MULTIPLE_STACK_H

#include <stdbool.h>

#define MAX_STACKS 3
#define STACK_SIZE 100

typedef struct {
    int data[STACK_SIZE];
    int top[MAX_STACKS];
    int base[MAX_STACKS];
    int limit[MAX_STACKS];
    int num_stacks;
} MultiStack;

void init_multi_stack(MultiStack* ms, int num_stacks);
bool push(MultiStack* ms, int stack_id, int value);
bool pop(MultiStack* ms, int stack_id, int* out);
void print_stack(MultiStack* ms, int stack_id);

#endif // MULTIPLE_STACK_H
