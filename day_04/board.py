#!/usr/bin/env python3
from typing import Optional
import re


class Board:
    """
    A bingo board.
    """

    def __init__(self, table_string: str):
        # Turn table_string into a matrix
        numbers_list = list(map(int, re.split(r"\s+", table_string.strip())))
        self.numbers = [[0] * 5 for i in range(5)]  # initialize all numbers to 0
        for i in range(len(numbers_list)):
            # Assign the real numbers
            self.numbers[i // 5][i % 5] = numbers_list[i]
        self.markers = [[False] * 5 for i in range(5)]

    def mark(self, number: int) -> bool:
        """
        Mark a number on the board. If it results in a win, return true. Else,
        return false.
        """
        coordinates = self.find(number)
        if coordinates:
            x, y = coordinates
            self.markers[y][x] = True
            return self.has_won()
        return False  # We didn't mark anything off, so we didn't win

    def find(self, number: int):
        for y in range(5):
            for x in range(5):
                if self.numbers[y][x] == number:
                    return (x, y)

    def has_won(self):
        return self.check_columns() or self.check_rows()

    def check_columns(self):
        """
        Returns true if a column is all filled out.
        """
        for x in range(5):
            if all([self.markers[y][x] for y in range(5)]):
                return True
        return False

    def check_rows(self) -> bool:
        """
        Returns true if a row is all filled out.
        """
        for y in range(5):
            if all(self.markers[y]):
                return True

        return False

    def unmarked_sum(self) -> int:
        """
        Get the sum of the unmarked numbers
        """
        total = 0
        for y in range(5):
            for x in range(5):
                if not self.markers[y][x]:
                    total += self.numbers[y][x]
        return total
