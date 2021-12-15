#!/usr/bin/env python3

from collections import Counter
from .rules import InsertionRules


def puzzle_1(template, rules):
    # polymer = grow_polymer(template, rules, 80)
    # elements = count_elements(polymer)
    # sorted = elements.most_common()
    # return sorted[0] - sorted[-1]
    total_elements = Counter()
    print(f"Total length: {len(template)}")
    for i in range(len(template) - 1):
        print(f"i: {i}")
        first_polymer = grow_polymer(template[i : i + 2], rules, 10)
        total_elements = total_elements + count_elements(first_polymer)

        for j in range(len(first_polymer) - 1):
            second_polymer = grow_polymer(first_polymer[j : j + 2], rules, 10)
            total_elements = total_elements + count_elements(second_polymer)

            for k in range(len(second_polymer) - 1):
                third_polymer = grow_polymer(second_polymer[k : k + 2], rules, 10)
                total_elements = total_elements + count_elements(third_polymer)

                for l in range(len(third_polymer) - 1):
                    fourth_polymer = grow_polymer(third_polymer[l : l + 2], rules, 10)
                    total_elements = total_elements + count_elements(fourth_polymer)

                    for m in range(len(fourth_polymer) - 1):
                        fifth_polymer = grow_polymer(
                            fourth_polymer[m : m + 2], rules, 10
                        )
                        total_elements = total_elements + count_elements(fifth_polymer)

                        for n in range(len(fifth_polymer) - 1):
                            print(f"  n: {n}")
                            sixth_polymer = grow_polymer(
                                fifth_polymer[n : n + 2], rules, 10
                            )
                            total_elements = total_elements + count_elements(
                                sixth_polymer
                            )

                            for o in range(len(sixth_polymer) - 1):
                                seventh_polymer = grow_polymer(
                                    sixth_polymer[o : o + 2], rules, 10
                                )
                                total_elements = total_elements + count_elements(
                                    seventh_polymer
                                )

                                for p in range(len(seventh_polymer) - 1):
                                    eighth_polymer = grow_polymer(
                                        seventh_polymer[p : p + 2], rules, 10
                                    )
                                    total_elements = total_elements + count_elements(
                                        eighth_polymer
                                    )

    sorted = total_elements.most_common()
    return sorted[0][1] - sorted[-1][1]


def puzzle_2(template, rules):
    pass


def memoize_count(func):
    memory = {}

    def inner(polymer):
        if polymer not in memory:
            memory[polymer] = func(polymer)
        return memory[polymer]

    return inner


@memoize_count
def count_elements(polymer):
    # Iterate over the string and increment each element count
    elements = {}
    for c in polymer:
        if c not in elements:
            elements[c] = 0
        elements[c] += 1

    return Counter(elements)


def memoize_grow(func):
    memory = {}

    def inner(template, rules, steps):
        if f"{template}-{steps}" not in memory:
            memory[f"{template}-{steps}"] = func(template, rules, steps)
        return memory[f"{template}-{steps}"]

    return inner


@memoize_grow
def grow_polymer(template, rules, steps):
    polymer = template
    for s in range(steps):
        new_polymer = [polymer[0]]  # Start with the first character
        for i in range(len(polymer) - 1):
            current_pair = polymer[i : i + 2]
            # Only add the new character and the second of the pair so we don't
            # double-add the second (when it's the first of the next pair)
            new_polymer.append(rules.get(current_pair) + current_pair[1])
        polymer = "".join(new_polymer)
    return polymer


def parse_input(puzzle_input):
    """
    Returns (template, rules)
    """
    template = puzzle_input[0]
    rules = InsertionRules(puzzle_input[2:])
    return (template, rules)


def run_puzzle(p, puzzle_input):
    template, rules = parse_input(puzzle_input)
    if p == 1:
        print(puzzle_1(template, rules))
    else:
        print(puzzle_2(template, rules))
