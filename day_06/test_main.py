#!/usr/bin/env python3

from .main import parse_input, age_fish

puzzle_input = ["3,4,3,1,2"]


def test_parse_input():
    assert parse_input(puzzle_input) == [
        0,  # 0 days
        1,  # 1 days
        1,  # 2 days
        2,  # ...
        1,
        0,
        0,
        0,
        0,  # 8 days
    ]


def test_age_fish_18():
    fish = parse_input(puzzle_input)
    for day in range(18):
        fish = age_fish(fish)
    assert sum(fish) == 26


def test_age_fish_80():
    fish = parse_input(puzzle_input)
    for day in range(80):
        fish = age_fish(fish)
    assert sum(fish) == 5934
