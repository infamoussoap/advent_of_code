import numpy as np


from utils.utils import readlines

FILENAME = 'data/day09.txt'


def non_zero_sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    return 1


class Grid:
    def __init__(self):
        self.head_pos = [0, 0]
        self.tail_pos = [0, 0]

        self.tail_pos_history = set()
        self.tail_pos_history.add(str(self.tail_pos))

    def move(self, direction, count=1):
        for _ in range(count):
            self._move_head(direction)

    def _move_head(self, direction):
        if direction == 'R':
            self.head_pos[1] += 1
        elif direction == 'L':
            self.head_pos[1] -= 1
        elif direction == 'U':
            self.head_pos[0] += 1
        elif direction == 'D':
            self.head_pos[0] -= 1
        else:
            raise ValueError(f"Direction {direction} not understood")

        self._update_tail()
        self.tail_pos_history.add(str(self.tail_pos))

    def _update_tail(self):
        if not self._is_head_touching_tail(self.head_pos, self.tail_pos):
            dx = self.head_pos[0] - self.tail_pos[0]
            dy = self.head_pos[1] - self.tail_pos[1]

            self.tail_pos[0] += non_zero_sign(dx)
            self.tail_pos[1] += non_zero_sign(dy)

    @staticmethod
    def _is_head_touching_tail(head_pos, tail_pos):
        if head_pos == tail_pos:
            return True

        dx = abs(head_pos[0] - tail_pos[0])
        dy = abs(head_pos[1] - tail_pos[1])

        return dx <= 1 and dy <= 1


class GridV2:
    def __init__(self):
        # Head is the first knot and the tail is the last knot
        self.knots_pos = [[0, 0].copy() for _ in range(10)]

        self.tail_pos_history = set()
        self.tail_pos_history.add(str(self.tail_pos))

    def move(self, direction, count=1):
        for _ in range(count):
            self._move_head(direction)

    def _move_head(self, direction):
        if direction == 'R':
            self.head_pos[1] += 1
        elif direction == 'L':
            self.head_pos[1] -= 1
        elif direction == 'U':
            self.head_pos[0] += 1
        elif direction == 'D':
            self.head_pos[0] -= 1
        else:
            raise ValueError(f"Direction {direction} not understood")

        self._update_tail_knots()
        self.tail_pos_history.add(str(self.tail_pos))

    def _update_tail_knots(self):
        for i in range(1, len(self.knots_pos)):
            self._update_knot(i)

    def _update_knot(self, i):
        assert i != 0, "Can't update the head in this method"

        previous_knot = self.knots_pos[i - 1]
        current_knot = self.knots_pos[i]

        if not self._is_knots_touching(previous_knot, current_knot):
            dx = previous_knot[0] - current_knot[0]
            dy = previous_knot[1] - current_knot[1]

            current_knot[0] += non_zero_sign(dx)
            current_knot[1] += non_zero_sign(dy)


    @staticmethod
    def _is_knots_touching(knot1, knot2):
        if knot1 == knot2:
            return True

        dx = abs(knot1[0] - knot2[0])
        dy = abs(knot1[1] - knot2[1])

        return dx <= 1 and dy <= 1

    @property
    def head_pos(self):
        return self.knots_pos[0]

    @property
    def tail_pos(self):
        return self.knots_pos[-1]



def part1():
    lines = readlines(FILENAME)

    grid = Grid()
    for line in lines:
        cleaned_line = line.replace('\n', '')

        direction, count = cleaned_line.split(' ')
        count = int(count)

        grid.move(direction, count)

    return len(grid.tail_pos_history)


def part2():
    lines = readlines(FILENAME)

    grid = GridV2()
    for line in lines:
        cleaned_line = line.replace('\n', '')

        direction, count = cleaned_line.split(' ')
        count = int(count)

        grid.move(direction, count)

    return len(grid.tail_pos_history)


if __name__ == '__main__':
    print("Advent of Code 2022 Day 09")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
