#!/usr/bin/env python3

# Get the arg for the day and the puzzle
# Run the appropriate function

import argparse
import os
from helpers.get_input import get_input

import day_01.main
import day_02.main
import day_03.main
import day_04.main

parser = argparse.ArgumentParser(description="Run a puzzle from a day.")
parser.add_argument("-d", help="The day", type=int, metavar="day")
parser.add_argument("-p", help="The puzzle", type=int, metavar="puzzle")

args = parser.parse_args()


# Check to make sure the input exists
if not os.path.exists(f"inputs/{args.d}.txt"):
    print(f"Found no puzzle input for day {args.d}. Fetching...")
    os.system(f"./get-input.sh {args.d}")

puzzle_input = get_input(args.d)

if args.d == 1:
    day_01.main.run_puzzle(args.p, puzzle_input)
if args.d == 2:
    day_02.main.run_puzzle(args.p, puzzle_input)
if args.d == 3:
    day_03.main.run_puzzle(args.p, puzzle_input)
if args.d == 4:
    day_04.main.run_puzzle(args.p, puzzle_input)
else:
    print(f"I can't find a function for day {args.d}")
