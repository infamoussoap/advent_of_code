from utils.utils import readlines

FILENAME = 'data/day14.txt'


def non_zero_sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


class Cave:
    def __init__(self):
        self.rock_locations = set()
        self.sand_locations = set()

        self.max_y = 0

    def add_rock_coordinates(self, coordinates):
        for coord1, coord2 in zip(coordinates[:-1], coordinates[1:]):
            x1, y1 = [int(x) for x in coord1.split(",")]
            x2, y2 = [int(x) for x in coord2.split(",")]

            self.add_rock_location(x1, y1)
            dx, dy = non_zero_sign(x1 - x2), non_zero_sign(y1 - y2)

            delta = abs(x1 - x2) + abs(y1 - y2)
            for i in range(1, delta + 1):
                self.add_rock_location(x1 - i * dx, y1 - i * dy)

    def add_rock_location(self, x, y):
        self.max_y = max(self.max_y, y)

        self.rock_locations.add(str((x, y)))

    def _is_location_blocked(self, x, y):
        return str((x, y)) in self.rock_locations or str((x, y)) in self.sand_locations

    def add_sand(self, x, y):
        if y > self.max_y:
            return False

        elif not self._is_location_blocked(x, y + 1):
            return self.add_sand(x, y + 1)

        elif not self._is_location_blocked(x - 1, y + 1):
            return self.add_sand(x - 1, y + 1)

        elif not self._is_location_blocked(x + 1, y + 1):
            return self.add_sand(x + 1, y + 1)

        else:
            self._add_sand_location(x, y)
            return True

    def _add_sand_location(self, x, y):
        self.sand_locations.add(str((x, y)))


class CaveV2:
    def __init__(self):
        self.rock_locations = set()
        self.sand_locations = set()

        self.max_y = 0

    def add_rock_coordinates(self, coordinates):
        for coord1, coord2 in zip(coordinates[:-1], coordinates[1:]):
            x1, y1 = [int(x) for x in coord1.split(",")]
            x2, y2 = [int(x) for x in coord2.split(",")]

            self.add_rock_location(x1, y1)
            dx, dy = non_zero_sign(x1 - x2), non_zero_sign(y1 - y2)

            delta = abs(x1 - x2) + abs(y1 - y2)
            for i in range(1, delta + 1):
                self.add_rock_location(x1 - i * dx, y1 - i * dy)

    def add_rock_location(self, x, y):
        self.max_y = max(self.max_y, y)

        self.rock_locations.add(str((x, y)))

    def _is_location_blocked(self, x, y):
        if y >= self.max_y + 2:
            return True

        return str((x, y)) in self.rock_locations or str((x, y)) in self.sand_locations

    def add_sand(self, x, y):
        if self._is_location_blocked(x, y):
            return False

        if not self._is_location_blocked(x, y + 1):
            return self.add_sand(x, y + 1)

        elif not self._is_location_blocked(x - 1, y + 1):
            return self.add_sand(x - 1, y + 1)

        elif not self._is_location_blocked(x + 1, y + 1):
            return self.add_sand(x + 1, y + 1)

        else:
            self._add_sand_location(x, y)
            return (x, y)

    def _add_sand_location(self, x, y):
        self.sand_locations.add(str((x, y)))



def part1():
    lines = readlines(FILENAME)

    cave = Cave()

    for line in lines:
        cleaned_line = line.replace('\n', '')
        coordinates = cleaned_line.split(" -> ")

        cave.add_rock_coordinates(coordinates)

    counter = 0
    while cave.add_sand(500, 0):
        counter += 1

    return counter


def part2():
    lines = readlines(FILENAME)

    cave = CaveV2()

    for line in lines:
        cleaned_line = line.replace('\n', '')
        coordinates = cleaned_line.split(" -> ")

        cave.add_rock_coordinates(coordinates)

    counter = 0
    while cave.add_sand(500, 0):
        counter += 1

    return counter


if __name__ == '__main__':
    print("Advent of Code 2022 Day 14")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
