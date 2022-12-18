from collections import defaultdict

from utils.day05 import read_file, parse_stack_line

FILENAME = 'data/day05.txt'


def move_item(elves, start_pos, end_pos):
    item = elves[start_pos].pop()
    elves[start_pos].append(item)


def move_items(elves, start_pos, end_pos, num_items=1):
    items = elves[start_pos]

    elves[end_pos] += items[-num_items:]
    elves[start_pos] = items[:-num_items]


def part1():
    starting_stacks, moves = read_file()

    num_elves = len(starting_stacks) + 1 // 3
    elves = defaultdict(list)

    for stacks in reversed(starting_stacks):
        for i, item in enumerate(parse_stack_line(stacks)):
            if item != '':
                elves[i].append(item)

    for move in moves:
        move_count, start_pos, end_pos = move.split(' ')[1::2]

        for _ in range(int(move_count)):
            move_item(elves, int(start_pos) - 1, int(end_pos) - 1)

    top_of_stack = ''
    for i in range (len(elves)):
        top_of_stack += elves[i][-1]

    return top_of_stack


def part2():
    starting_stacks, moves = read_file()

    num_elves = len(starting_stacks) + 1 // 3
    elves = defaultdict(list)

    for stacks in reversed(starting_stacks):
        for i, item in enumerate(parse_stack_line(stacks)):
            if item != '':
                elves[i].append(item)


    for move in moves:
        move_count, start_pos, end_pos = move.split(' ')[1::2]

        move_items(elves, int(start_pos) - 1, int(end_pos) - 1, int(move_count))

    top_of_stack = ''
    for i in range (len(elves)):
        top_of_stack += elves[i][-1]

    return top_of_stack


if __name__ == '__main__':
    print("Advent of Code 2022 Day 05")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
