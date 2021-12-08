#!/usr/bin/env python3

from .board import Board


board_input = """22 13 17 11  0
8  2 23  4 24
21  9 14 16  7
6 10  3 18  5
1 12 20 15 19"""


parsed = [
    [22, 13, 17, 11, 0],
    [8, 2, 23, 4, 24],
    [21, 9, 14, 16, 7],
    [6, 10, 3, 18, 5],
    [1, 12, 20, 15, 19],
]


def test_init():
    b = Board(board_input)
    assert b.numbers == parsed


def test_mark():
    b = Board(board_input)
    b.mark(22)
    assert b.markers[0][0] == True
    b.mark(23)
    assert b.markers[1][2] == True
    b.mark(19)
    assert b.markers[4][4] == True


def test_row_win():
    # Test every row
    for y in range(5):
        b = Board(board_input)
        for x in range(4):
            b.mark(parsed[y][x])
        # Expect the marking the last number in the row to return a win
        assert b.mark(parsed[y][4]) == True


def test_col_win():
    for x in range(5):
        b = Board(board_input)
        for y in range(4):
            b.mark(parsed[y][x])
        # Expect marking the last number in the column to return a win
        assert b.mark(parsed[4][x]) == True


def test_unmarked_sum():
    b = Board(board_input)

    # Mark off every number except the first row
    for y in range(1, 5):
        for x in range(5):
            b.mark(parsed[y][x])
    assert b.unmarked_sum() == 22 + 13 + 17 + 11
