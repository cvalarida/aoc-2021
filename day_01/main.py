#!/usr/bin/env python3


def puzzle_1(puzzle_input):
    count = 0
    for i in range(1, len(puzzle_input)):
        if puzzle_input[i] > puzzle_input[i - 1]:
            count += 1

    print(count)


def puzzle_2(puzzle_input):
    inputs = []
    for i in range(2, len(puzzle_input)):
        inputs.append(puzzle_input[i] + puzzle_input[i - 1] + puzzle_input[i - 2])

    puzzle_1(inputs)


def run_puzzle(p, puzzle_input):
    puzzle_input = list(map(int, puzzle_input))
    if p == 1:
        puzzle_1(puzzle_input)
    else:
        puzzle_2(puzzle_input)
