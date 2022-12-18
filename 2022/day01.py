import numpy as np
from collections import defaultdict

from utils.utils import readlines


FILENAME = 'data/day01.txt'


def get_elves_carrying_calories():
    lines = readlines(FILENAME)

    elves = defaultdict(int)
    current_elf = 1

    for line in lines:
        cleaned_line = line.replace('\n', '')

        if len(cleaned_line) == 0:
            current_elf += 1
        else:
            elves[current_elf] += int(cleaned_line)

    return elves


def part1():
    elves = get_elves_carrying_calories()
    return max(list(elves.values()))


def part2():
    elves = get_elves_carrying_calories()

    total_calories = list(elves.values())
    total_calories = sorted(total_calories, reverse=True)

    return sum(total_calories[:3])


if __name__ == '__main__':
    print("Advent of Code 2022 Day 01")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
