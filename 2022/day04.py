from utils.utils import readlines

FILENAME = 'data/day04.txt'


class Section:
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)

    def contains(self, section):
        return self.start <= section.start and section.end <= self.end

    def overlaps(self, section):
        return self._in(section.start) or self._in(section.end)

    def _in(self, index):
        return self.start <= index <= self.end


def part1():
    lines = readlines(FILENAME)

    counter = 0

    for line in lines:
        cleaned_line = line.replace('\n', '')

        assignment1, assignment2 = cleaned_line.split(',')

        section1 = Section(*assignment1.split('-'))
        section2 = Section(*assignment2.split('-'))

        counter += section1.contains(section2) or section2.contains(section1)

    return counter


def part2():
    lines = readlines(FILENAME)

    counter = 0

    for line in lines:
        cleaned_line = line.replace('\n', '')

        assignment1, assignment2 = cleaned_line.split(',')

        section1 = Section(*assignment1.split('-'))
        section2 = Section(*assignment2.split('-'))

        counter += section1.overlaps(section2) or section2.overlaps(section1)

    return counter


if __name__ == '__main__':
    print("Advent of Code 2022 Day 04")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
