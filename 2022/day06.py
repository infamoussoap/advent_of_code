from utils.utils import readlines

FILENAME = 'data/day06.txt'


def part1():
    datastream = readlines(FILENAME)[0]

    for i in range(4, len(datastream)):
        packet = datastream[i - 4 : i]
        if len(set(packet)) == 4:
            return i, packet


def part2():
    datastream = readlines(FILENAME)[0]

    for i in range(14, len(datastream)):
        packet = datastream[i - 14 : i]
        if len(set(packet)) == 14:
            return i, packet


if __name__ == '__main__':
    print("Advent of Code 2022 Day 06")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
