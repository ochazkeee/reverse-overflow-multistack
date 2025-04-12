# Reverse Overflow-Based Multiple Stack

## Overview  
This project introduces a space-efficient data structure that enables **multiple stacks to coexist in a single array**, sharing memory intelligently.  
When a stack exceeds its own region, it can intrude into the free space of neighboring stacks **in reverse direction** — a strategy we call **Reverse Overflow**.

Compared to traditional equal partitioning, this approach offers significantly better space utilization and handles various scenarios without dynamic resizing.

## Features

- **Reverse Overflow Algorithm**  
  All stacks share a single fixed-size array. Each stack grows in its assigned direction, and if space runs out, it overflows *in reverse* into adjacent stack space.

- **No Dynamic Memory Allocation**  
  Operates entirely within a statically allocated array, maximizing memory efficiency.

- **Pop & Reclaim Logic**  
  When elements are popped, the structure reclaims and readjusts space, making it available for future pushes.

- **Performance Comparisons**  
  Benchmark results comparing this method with equal partitioning and Knuth’s linked stack can be found in [`docs/en/comparison.md`](./docs/en/comparison.md).

## Directory Structure

```
reverse-overflow-multistack/
├── README.md                  # Main project introduction (English)
├── README.ko.md               # Korean summary version
├── LICENSE
├── docs/
│   ├── en/
│   │   ├── structure.md       # Core concepts and algorithm design
│   │   ├── comparison.md      # Performance evaluation and comparison
│   │   ├── implementation.md  # Code-level implementation notes
│   │   └── faq.md             # Frequently asked questions
│   └── ko/
│       ├── structure.ko.md
│       ├── comparison.ko.md
│       ├── implementation.ko.md
│       └── faq.ko.md
├── src/                       # C source code
│   ├── main.c
│   ├── multiple_stack.c
│   └── multiple_stack.h
├── benchmarks/                # Python scripts for performance testing
│   ├── implementations.py
│   ├── test.py
│   └── images/                # Experimental result visualizations
│       ├── experiment_0.png
│       ├── experiment_1.png
│       ├── experiment_2.png
│       ├── experiment_3.png
│       └── experiment_4.png
└── CMakeLists.txt             # CMake build configuration
```



## Documentation

- [`structure.md`](./docs/en/structure.md) – Structure and core algorithm  
- [`comparison.md`](./docs/en/comparison.md) – Comparison with existing methods and trade-offs  
- [`implementation.md`](./docs/en/implementation.md) – Implementation details and logic  
- [`faq.md`](./docs/en/faq.md) – Frequently Asked Questions

## How to Build

```bash
mkdir build
cd build
cmake ..
make
./reverse_stack_demo
```

## Notes & Contribution Guide

This project is a work in progress and is based on theoretical ideas and experimental implementation.  
The Reverse Overflow strategy is one possible method to improve memory efficiency for multi-stack systems.

The project is licensed under the [MIT License](./LICENSE), and you are welcome to use, modify, and distribute it freely.  
If you have feedback or suggestions, feel free to [open an issue](https://github.com/ochazkeee/reverse-overflow-multistack/issues) or contribute via pull request.

> We welcome **constructive feedback, discussions, and alternative proposals**.  
> While the implementation is still evolving, this project is an open platform for learning, exploration, and community collaboration. Your input is highly appreciated!
