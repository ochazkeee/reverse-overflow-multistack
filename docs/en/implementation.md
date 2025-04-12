# Implementation Details and Algorithm Description

## Overview

This document explains the internal implementation and algorithm of the **Reverse Overflow-based Multiple Stack data structure**.  
This structure enables multiple stacks to **dynamically share space** within a single fixed-size array.  
Each stack uses its own base region first, but when the space runs out, it **searches adjacent stacks’ unused areas in reverse order** and overflows into them.  
The system also includes a **reclaim mechanism** that restores invaded space during the pop operation.

---

## Data Structures

### 1. Base Array and Stack State Structures

- **arr (array)**  
  A fixed-size one-dimensional array shared by all stacks.  
  All push/pop operations are performed on this array.

- **starts[], ends[] (stack range)**  
  Arrays that store the starting and ending index of each stack’s base area.  
  Example: `starts[i] = 0`, `ends[i] = 99`

- **tops[] (top indices)**  
  Array indicating the current top index of each stack.

- **owner[] (specific to Reverse Overflow)**  
  Indicates which stack owns each cell of the array.  
  `-1` means unused, while `0`, `1`, ..., `n-1` indicate stack ownership.

- **free_indices (optional)**  
  An auxiliary structure (like a heap or queue) to efficiently track empty indices  
  and quickly locate available space.

---

## Algorithm Workflow

### 1. Push Operation

1. **Within Base Region**  
   - If `tops[i] + 1 <= ends[i]` and the next cell is empty, perform a normal push.  
   - Update: `arr[next_pos] = value`, `owner[next_pos] = i`, `tops[i]++`

2. **Reverse Overflow Condition**  
   - If the base region is full, search for available space in adjacent stacks  
     in **reverse order** (from end to start).  
   - Use the nearest available space, update ownership, and adjust `tops[i]`.

3. **Overflow Failure**  
   - If no space is available anywhere, return `FAILURE` or trigger an exception.

---

### 2. Pop Operation

1. **Normal or Overflow Area Pop**  
   - If `tops[i] >= starts[i]`, pop the value from the top.  
   - Update: clear the value, reset ownership, and decrement the top index.

2. **Reclaim Logic**  
   - If the popped cell lies **outside of the base region**,  
     use the `owner[]` array to **restore the invaded area**  
     back to the original adjacent stack’s territory.

---

## Pseudocode Example

```plaintext
function push(stack, value):
    next_pos = tops[stack] + 1
    if next_pos <= ends[stack] and arr[next_pos] is empty:
        arr[next_pos] = value
        owner[next_pos] = stack
        tops[stack] = next_pos
        return SUCCESS
    else:
        // Reverse Overflow Search
        for i from array.length - 1 to 0:
            if arr[i] is empty:
                arr[i] = value
                owner[i] = stack
                tops[stack] = i
                return SUCCESS
        return FAILURE

function pop(stack):
    if tops[stack] < starts[stack]:
        return UNDERFLOW
    value = arr[tops[stack]]
    arr[tops[stack]] = null
    owner[tops[stack]] = -1
    // Reclaim logic if necessary
    if tops[stack] not in base area of stack:
        // Handle restore (optional)
    tops[stack] = tops[stack] - 1
    return value
