#!/usr/bin/env python3
from .main import travel_vent, draw_vents, parse_input, puzzle_1


def test_travel_distance_y_pos():
    line = (0, 0, 0, 5)
    correct = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
    ]
    assert [(x, y) for x, y in travel_vent(line)] == correct


def test_travel_distance_y_neg():
    line = (0, 5, 0, 0)
    correct = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
    ]
    assert [(x, y) for x, y in travel_vent(line)] == correct


def test_travel_distance_x_pos():
    line = (0, 0, 5, 0)
    correct = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
    ]
    assert [(x, y) for x, y in travel_vent(line)] == correct


def test_travel_distance_y_neg():
    line = (5, 0, 0, 0)
    correct = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
    ]
    assert [(x, y) for x, y in travel_vent(line)] == correct


puzzle_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def test_draw_vents():
    ocean_floor = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0,],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0,],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0,],
        [0, 1, 1, 2, 1, 1, 1, 2, 1, 1,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [2, 2, 2, 1, 1, 1, 0, 0, 0, 0,],
    ]
    assert draw_vents(parse_input(puzzle_input)) == ocean_floor


def test_puzzle_1():
    assert puzzle_1(parse_input(puzzle_input)) == 5
