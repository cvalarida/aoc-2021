#!/usr/bin/env python3


def puzzle_1(crabs):
    smallest = float("inf")
    # Add all the positions to a set
    # Iterate over that set and sum the distance needed
    # Keep the smallest
    for pos in set(crabs):
        smallest = min(smallest, sum([abs(c - pos) for c in crabs]))
    return smallest


def puzzle_2(crabs):
    smallest = float("inf")
    # Oh man, is this sloooooow. But the answer isn't an existing position, so...
    for pos in range(max(*crabs)):
        smallest = min(smallest, sum([sum(range(abs(c - pos) + 1)) for c in crabs]))
    return smallest


def parse_input(puzzle_input):
    return list(map(int, puzzle_input[0].split(",")))


def run_puzzle(p, puzzle_input):
    crabs = parse_input(puzzle_input)
    if p == 1:
        print(puzzle_1(crabs))
    else:
        print(puzzle_2(crabs))
