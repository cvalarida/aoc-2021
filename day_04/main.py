#!/usr/bin/env python3
from .board import Board


def puzzle_1(numbers, boards):
    for n in numbers:
        for i in range(len(boards)):
            if boards[i].mark(n):
                print(boards[i].unmarked_sum() * n)
                return  # The ith board won first!


def puzzle_2(numbers, tables):
    pass


def parse_input(puzzle_input):
    chunks = puzzle_input.split("\n\n")
    numbers = list(map(int, chunks[0].split(",")))
    boards = list(map(Board, chunks[1:]))
    return numbers, boards


def run_puzzle(p, puzzle_input):
    numbers, tables = parse_input(puzzle_input)
    if p == 1:
        puzzle_1(numbers, tables)
    else:
        puzzle_2(numbers, tables)
