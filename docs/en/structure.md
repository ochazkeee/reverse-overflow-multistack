# Structure and Algorithm Overview

## Overview

This document outlines the core concepts and internal design of the Reverse Overflow-based Multiple Stack data structure.  
This structure allows multiple stacks to **share space within a single fixed-size array**,  
proposed as an alternative to conventional **equal partitioning** methods that suffer from memory waste.

---

## Core Idea

- Each stack begins at a specific position within the array and grows in **its own direction**.
- By default, stacks grow without interference. However, when space runs low,  
  the **Reverse Overflow** logic allows a stack to **explore and use unused space** of an adjacent stack in the reverse direction.
- During `pop` operations, the overflowed space is reclaimed to **preserve the original layout as much as possible**.

---

## Example: Stack Layout in a Shared Array

Here's an example of four stacks (S0, S1, S2, S3) **sharing space in a single array**,  
growing in opposite directions:

### Array Index

[ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ]

### Stack Placement and Growth Directions

<pre> ``` |→ S0 →|← S1 ←| |→ S2 →|← S3 ←| [ 0 ... 7 ][ 8 ... 15 ] ``` </pre>

---

## Stack Descriptions

- **S0**: Grows from the left to right (→) *(forward direction)*  
- **S1**: Grows from the right to left (←), adjacent to S0 *(reverse direction)*  
- **S2**: Grows from the right-side region toward the center (→) *(forward direction)*  
- **S3**: Grows from the far right to the left (←) *(reverse direction)*  

Each stack can intrude into adjacent stacks via the **Reverse Overflow** strategy,  
allowing **dynamic space sharing within a fixed-size array**.

---

## Space Sharing Strategy

Even if the array has 16 slots in total,  
**each stack is not fixed to 4 slots**.  
Instead, **space is allocated dynamically** based on real-time usage.

Example:  
- If S0 uses 6 slots and S1 uses only 1 slot,  
  → S0 can overflow into S1's unused space.

---

## Summary of Advantages

- **Optimized memory usage**: Dynamically grows as needed  
- **Reuses idle space** with Reverse Overflow  
- **Flexible stack behavior within a static array**  
- **Structural stability is maintained during `pop` operations**

---

The next document, [`implementation.md`](./implementation.md), will provide a detailed explanation  
of how this structure is implemented and the algorithms used.
