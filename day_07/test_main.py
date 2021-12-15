#!/usr/bin/env python3

from .main import puzzle_2

puzzle_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_puzzle_2():
    assert puzzle_2(puzzle_input) == 168
