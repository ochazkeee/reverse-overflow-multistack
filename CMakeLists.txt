cmake_minimum_required(VERSION 3.10)

project(MultipleStackReverseOverflow C)

set(CMAKE_C_STANDARD 99)

add_executable(my_stack_app
    src/main.c
    src/multiple_stack.c
)
