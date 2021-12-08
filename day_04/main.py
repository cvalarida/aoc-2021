#!/usr/bin/env python3
from .board import Board


def puzzle_1(numbers, boards):
    for n in numbers:
        for i in range(len(boards)):
            if boards[i].mark(n):
                print(boards[i].unmarked_sum() * n)
                return  # The ith board won first!


def puzzle_2(numbers, boards):
    table_wins = [False] * len(boards)
    last_board_won = -1
    winning_number = -1
    for n in numbers:
        for i in range(len(boards)):
            if not table_wins[i] and boards[i].mark(n):
                # This board just won for the firs time!
                last_board_won = i
                winning_number = n
                table_wins[i] = True
                if all(table_wins):
                    break  # Just...stop if we can

    print(boards[last_board_won].unmarked_sum() * winning_number)


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
