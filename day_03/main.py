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
    count = count_ones(data, pos)
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


def count_ones(data, pos):
    count = 0
    for bits in data:
        count += bits[pos]
    return count


# def filter_by_commonality(data, pos, value):
#     # Return only items in the array whose bit at the position is equal to the value
#     result = []
#     # Get the common bit
#     ones = count_ones(data, pos)
#     # If:
#     #   - The current bit matches the majority bit
#     #   - There is no majority bit and the current bit is 1
#     for d in data:
#         if ones >= len(data) / 2:
#             # Ones are the most common (or equal)
#             if value == "most" and d[pos] == 1:
#                 result.append(d)
#         if ones <= len(data) / 2:
#             # Zeros are the most common (or equal)
#     return result


def get_most_common(data, pos):
    result = []
    ones = count_ones(data, pos)
    keep_bit = 0 if ones < len(data) / 2 else 1
    for d in data:
        if d[pos] == keep_bit:
            result.append(d)
    return result


def get_least_common(data, pos):
    result = []
    ones = count_ones(data, pos)
    keep_bit = 1 if ones < len(data) / 2 else 0
    for d in data:
        if d[pos] == keep_bit:
            result.append(d)
    return result


def puzzle_2(data):
    oxygen_list = data
    co2_list = data

    for i in range(len(data[0])):
        oxygen_list = get_most_common(oxygen_list, i)
    for i in range(len(data[0])):
        co2_list = get_least_common(co2_list, i)
        if len(co2_list) == 1:
            break

    result = bits_to_dec(oxygen_list[0]) * bits_to_dec(co2_list[0])
    print(result)


def run_puzzle(p, puzzle_input):
    binary_stream = []
    for l in puzzle_input:
        bits = list(map(int, l))  # Convert '010101' into [0, 1, 0, 1, 0, 1]
        binary_stream.append(bits)

    if p == 1:
        puzzle_1(binary_stream)
    else:
        puzzle_2(binary_stream)
