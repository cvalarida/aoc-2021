#!/usr/bin/env python3
from typing import List
import re

# AB -> C
# (AB, C)
Rule = tuple[str, str]


class InsertionRules:
    def __init__(self, rules: List[str]):
        self.pair_map = {}
        for rule in rules:
            pair, result = re.search(r"(\w\w) -> (\w)", rule).groups()
            self.pair_map[pair] = result

    def get(self, pair: str) -> str:
        return self.pair_map[pair]
