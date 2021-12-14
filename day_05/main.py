#!/usr/bin/env python3
#
# This is admittedly ugly, but I don't care enough to make it better.
import re


def puzzle_1(vents):
    ocean_floor = draw_vents(vents)
    overlaps = 0
    for y in range(len(ocean_floor)):
        for x in range(len(ocean_floor[y])):
            if ocean_floor[y][x] > 1:
                overlaps += 1
    return overlaps


def puzzle_2(vents):
    ocean_floor = draw_vents(vents, True)
    overlaps = 0
    for y in range(len(ocean_floor)):
        for x in range(len(ocean_floor[y])):
            if ocean_floor[y][x] > 1:
                overlaps += 1
    return overlaps


def draw_vents(vents, plot_diagonals=False):
    """
    Returns the ocean floor of dimensions equal to the largest x and y found in vents.
    Also ~returns~ should return the largest number of intersecting vents.
    """
    largest_x = 0
    largest_y = 0
    for vent in vents:
        x1, y1, x2, y2 = vent
        largest_x = max(largest_x, x1, x2)
        largest_y = max(largest_y, y1, y2)

    # Initialize the ocean floor dimensions; everything starts at 0
    ocean_floor = [[0 for x in range(largest_x + 1)] for y in range(largest_y + 1)]

    for vent in vents:
        x1, y1, x2, y2 = vent
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if x1 == x2 or y1 == y2 or (plot_diagonals and dx == dy):
            for x, y in travel_vent(vent):
                ocean_floor[y][x] += 1

    return ocean_floor


def travel_vent(line):
    """
    Travel an orthagonal line. Generator function returning coordinates (x, y) for
    line (x1, y1, x2, y2).
    """
    x1, y1, x2, y2 = line
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx > dy:
        return travel_horizontal(line)
    elif dy > dx:
        return travel_vertical(line)
    else:
        return travel_diagonal(line)


def travel_horizontal(line):
    x1, y1, x2, y2 = line
    smallest = min(x1, x2)
    largest = max(x1, x2)
    for x in range(smallest, largest + 1):
        yield (x, y1)


def travel_vertical(line):
    x1, y1, x2, y2 = line
    smallest = min(y1, y2)
    largest = max(y1, y2)
    for y in range(smallest, largest + 1):
        yield (x1, y)


def travel_diagonal(line):
    x1, y1, x2, y2 = line
    x_direction = 1 if x1 < x2 else -1
    y_direction = 1 if y1 < y2 else -1
    dx = range(x1, x2 + x_direction, x_direction)
    dy = range(y1, y2 + y_direction, y_direction)
    for x, y in zip(dx, dy):
        yield (x, y)


def parse_input(puzzle_input):
    """
    Take the string array (linewise) and parse it into (x1, y1, x2, y2).
    """
    lines = []
    for l in puzzle_input:
        result = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", l)
        lines.append(tuple(map(int, result.groups())))
    return lines


def run_puzzle(p, puzzle_input):
    vents = parse_input(puzzle_input)
    if p == 1:
        print(puzzle_1(vents))
    else:
        print(puzzle_2(vents))
