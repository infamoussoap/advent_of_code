import numpy as np
from functools import reduce

from utils.utils import readlines


FILENAME = 'data/day03.txt'


NUM_ITEMS = ord('z') - ord('A') + 1

def count_items(item):
    counter = np.zeros(NUM_ITEMS)

    for char in item:
        counter[ord(char) - ord('A')] += 1

    return counter

def get_common_items(item1, item2):
    counted_items1 = count_items(item1)
    counted_items2 = count_items(item2)

    common_items_index = np.argwhere(counted_items1 * counted_items2).flatten()

    return [chr(x + ord('A')) for x in common_items_index]

def get_common_items_v2(*items):
    """ Rewritten to accept an arbitrary amount of items """
    indexed_items = [count_items(item_list) for item_list in items]

    common_items = reduce(lambda x, y: x * y, indexed_items, 1)
    common_items_index = np.argwhere(common_items).flatten()

    return [chr(x + ord('A')) for x in common_items_index]

def item_priority(item):
    if ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27

    return ord(item) - ord('a') + 1


def part1():
    lines = readlines(FILENAME)

    counter = 0

    for line in lines:
        cleaned_line = line.replace("\n", "")

        middle_index = len(cleaned_line) // 2

        item1 = cleaned_line[:middle_index]
        item2 = cleaned_line[middle_index:]

        common_items = get_common_items(item1, item2)

        counter += sum([item_priority(item) for item in common_items])

    return counter


def part2():
    lines = readlines(FILENAME)

    current_rucksack = []
    line_counter = 0
    counter = 0

    for line in lines:
        cleaned_line = line.replace("\n", "")

        line_counter += 1
        current_rucksack.append(cleaned_line)

        if line_counter == 3:
            common_items = get_common_items_v2(*current_rucksack)
            counter += sum([item_priority(item) for item in common_items])

            line_counter = 0
            current_rucksack = []

    return counter


if __name__ == '__main__':
    print("Advent of Code 2022 Day 03")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
