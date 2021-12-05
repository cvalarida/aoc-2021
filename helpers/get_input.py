# Get the input for a day as an array

import os.path


def get_input(day: int) -> list:
    with open(os.path.join(os.path.dirname(__file__), f"../inputs/{day}.txt")) as f:
        return f.read().splitlines()
