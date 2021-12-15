#!/usr/bin/env python3

from .main import parse_input, grow_polymer

puzzle_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split(
    "\n"
)


def test_parse_input():
    template, rules = parse_input(puzzle_input)
    assert template == "NNCB"
    assert rules.pair_map == {
        "CH": "B",
        "HH": "N",
        "CB": "H",
        "NH": "C",
        "HB": "C",
        "HC": "B",
        "HN": "C",
        "NN": "C",
        "BH": "H",
        "NC": "B",
        "NB": "B",
        "BN": "B",
        "BB": "N",
        "BC": "B",
        "CC": "N",
        "CN": "C",
    }


def test_grow_polymer():
    template, rules = parse_input(puzzle_input)
    assert (
        grow_polymer(template, rules, 4)
        == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
    )
