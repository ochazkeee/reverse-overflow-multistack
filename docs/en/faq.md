# Frequently Asked Questions (FAQ)

## What is this structure used for?

The Reverse Overflow-based Multiple Stack structure is useful when multiple stacks need to be implemented efficiently within a fixed-size array.  
It is especially suitable for environments with limited memory, such as embedded systems, where avoiding memory waste is critical.

---

## How is this different from traditional equal partitioning?

Traditional methods divide the entire array into equal fixed-size regions, each allocated to a specific stack.  
However, when some stacks fill up quickly, unused space in other stacks is wasted.

The Reverse Overflow approach allows each stack to grow in its assigned direction and, when space runs out, to intrude into adjacent stacks’ unused space in the reverse direction.  
This dramatically improves memory utilization.

---

## Q: What is the difference between the Reverse Overflow method and Flexible Equal Partitioning?

**A:** Both methods aim to dynamically reallocate memory to improve efficiency in multiple stack implementations, but they differ in several key aspects:

- **Expansion Direction:**  
  - The **Flexible Equal Partitioning** approach typically divides the entire array into equal parts, and when a stack becomes full, it expands into the adjacent region in the forward direction.
  - In contrast, the **Reverse Overflow** method allows a stack to search for and intrude into the unused space of a neighboring stack **in the reverse direction** when its own region is insufficient.

- **Reclaim Mechanism:**  
  - With Flexible Equal Partitioning, when a stack’s allocated region is exhausted, the overall rebalancing or resizing of regions can be required, potentially incurring significant overhead.
  - The Reverse Overflow method automatically reclaims the overflowed space during a pop operation, preserving the original structure as much as possible without requiring a full region reallocation.

- **Implementation Strategy:**  
  - Flexible Equal Partitioning statically divides the array, which may lead to wasted memory if one stack fills up much faster than the others.
  - The Reverse Overflow approach maintains the basic boundaries of each stack while allowing temporary borrowing of space from adjacent regions. This results in a more flexible and efficient usage of the available memory.

In summary, the Reverse Overflow method distinguishes itself by not only allowing dynamic space sharing but also by integrating precise logic for both overflow and subsequent reclamation, thereby maximizing overall memory utilization.

---

## How does it perform in practice?

The `benchmarks/` directory contains Python scripts for evaluating and comparing different implementations.  
Initial test results show that the Reverse Overflow structure provides a significant advantage in space efficiency over equal partitioning.

In terms of time complexity, there may be slight overhead due to the reclaim and search logic, but optimizations help maintain solid performance.  
See `docs/comparison.md` for detailed comparison results.

---

## Is it safe for a stack to invade another?

Yes — the overflow logic operates under strict rules:

- Only unused space in adjacent stacks is explored.
- Protection mechanisms prevent intrusion into active stack areas.
- The `pop` operation triggers a reclaim mechanism to return overflowed space.

However, this implementation is still experimental and undergoing testing to validate edge cases and robustness.

---

## Is this structure scalable?

Yes. The structure is designed to allow dynamic configuration of the number of stacks.  
Even without resizing the array, it’s possible to adjust stack count or modify growth directions, offering flexibility for various applications.

---

## How can I contribute to this structure?

This project is released under the MIT License and is open for free use, modification, and distribution.  
If you have suggestions or improvements in mind, feel free to [open an issue](https://github.com/ochazkeee/reverse-overflow-multistack/issues) or submit a Pull Request (PR).

All forms of contributions are welcome — including structure design, code refactoring, test case development, and documentation.

---

## Is this structure original?

The Reverse Overflow strategy is not commonly found in data structure textbooks or typical implementations.  
As far as we know, the combination of **reverse-direction overflow with reclaim logic** in multi-stack array structures is rare.

That said, if you’re aware of similar prior work, we’d greatly appreciate a reference.

This project is part of an ongoing learning and experimentation effort and is published to encourage idea sharing and discussion.
