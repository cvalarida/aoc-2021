#!/usr/bin/env python3


def puzzle_1(commands):
    x = 0
    y = 0
    for command, value in commands:
        value = int(value)
        if command == "forward":
            x += value
        if command == "down":
            y += value
        if command == "up":
            y -= value

    solution = x * y
    print(solution)


def puzzle_2(commands):
    x = 0
    y = 0
    aim = 0
    for command, value in commands:
        value = int(value)
        if command == "forward":
            x += value
            y += aim * value
        if command == "down":
            aim += value
        if command == "up":
            aim -= value

    solution = x * y
    print(solution)


def run_puzzle(p, puzzle_input):
    puzzle_input = list(map(lambda l: l.split(), puzzle_input))
    if p == 1:
        puzzle_1(puzzle_input)
    else:
        puzzle_2(puzzle_input)
