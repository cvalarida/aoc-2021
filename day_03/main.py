#!/usr/bin/env python3

import math

# Takse an array of 0s and 1s and translates it into an int
def bits_to_dec(bits):
    total = 0
    for i in range(len(bits)):
        # bits[-1] = 2^0
        total += bits[i] * pow(2, len(bits) - (i + 1))
    return total


# Iterate through the bits and add the bits[pos] together
# Compare to the len(data)
def most_common(data, pos):
    count = 0
    for bits in data:
        count += bits[pos]
    return int(count > len(data) / 2)  # What if they're even?


def puzzle_1(data):
    # Find the most common of each bit
    gamma = []
    epsilon = []
    for i in range(len(data[0])):
        common_bit = most_common(data, i)
        gamma.append(common_bit)
        epsilon.append(int(not common_bit))

    gamma_dec = bits_to_dec(gamma)
    epsilon_dec = bits_to_dec(epsilon)
    print(gamma_dec * epsilon_dec)


def puzzle_2(data):
    pass


def run_puzzle(p, puzzle_input):
    binary_stream = []
    for l in puzzle_input:
        bits = list(map(int, l))  # Convert '010101' into [0, 1, 0, 1, 0, 1]
        binary_stream.append(bits)

    if p == 1:
        puzzle_1(binary_stream)
    else:
        puzzle_2(binary_stream)
