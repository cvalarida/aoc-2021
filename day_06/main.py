#!/usr/bin/env python3


def puzzle_1(fish):
    for day in range(80):
        fish = age_fish(fish)
    return sum(fish)


def puzzle_2(fish):
    for day in range(256):
        fish = age_fish(fish)
    return sum(fish)


def age_fish(fish):
    new_fish = [0] * 9
    # Day 0 spawns new fish and resets their own timer
    new_fish[8] = fish[0]
    new_fish[6] = fish[0]
    for day in range(1, len(fish)):
        new_fish[day - 1] += fish[day]  # Another day older and deeper in debt
    return new_fish


def parse_input(puzzle_input):
    fish = [0] * 9
    for f in puzzle_input[0].split(","):
        fish[int(f)] += 1
    return fish


def run_puzzle(p, puzzle_input):
    fish = parse_input(puzzle_input)
    if p == 1:
        print(puzzle_1(fish))
    else:
        print(puzzle_2(fish))
