#!/usr/bin/env python3

# Get the arg for the day and the puzzle
# Run the appropriate function

import argparse
import os
import day_01.main

parser = argparse.ArgumentParser(description="Run a puzzle from a day.")
parser.add_argument("-d", help="The day", type=int, metavar="day")
parser.add_argument("-p", help="The puzzle", type=int, metavar="puzzle")

args = parser.parse_args()


# Check to make sure the input exists
if not os.path.exists(f"inputs/{args.d}.txt"):
    print(f"Found no puzzle input for day {args.d}. Fetching...")
    os.system(f"./get-input.sh {args.d}")


if args.d == 1:
    day_01.main.run_puzzle(args.p)
else:
    print(f"I can't find a function for day {args.d}")
