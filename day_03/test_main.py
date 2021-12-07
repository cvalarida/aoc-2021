#!/usr/bin/env python3

from .main import puzzle_2


def test_puzzle_2():
    data = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    binary_stream = []
    for l in data:
        bits = list(map(int, l))  # Convert '010101' into [0, 1, 0, 1, 0, 1]
        binary_stream.append(bits)
    assert puzzle_2(binary_stream) == 230
