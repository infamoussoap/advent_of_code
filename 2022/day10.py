from utils.utils import readlines

FILENAME = 'data/day10.txt'


class Register:
    def __init__(self):
        self.X = 1
        self.started_cycle = 0
        self.completed_cycle = 0

        self.history = []

    def __call__(self, instruction):
        if instruction == "noop":
            self._cycle_register()
        else:
            _, val = instruction.split(" ")

            self._cycle_register()
            self._cycle_register(int(val))

    def _cycle_register(self, val=None):
        self.started_cycle += 1
        self._save_register_value()

        if val is not None:
            self.X += val

        self.completed_cycle += 1

    def _save_register_value(self):
        if (self.started_cycle - 20) % 40 == 0:
            self.history.append(self.X * self.started_cycle)


class CRT:
    def __init__(self):
        self.sprite_position = 1

        self.started_cycle = 0
        self.completed_cycle = 0

        self.drawn_pixels = ['']

    def __call__(self, instruction):
        if instruction == "noop":
            self._cycle_register()
        else:
            _, val = instruction.split(" ")

            self._cycle_register()
            self._cycle_register(int(val))

    def _cycle_register(self, val=None):
        self.started_cycle += 1
        self._draw_pixel()

        if val is not None:
            self.sprite_position += val

        self.completed_cycle += 1

    def _draw_pixel(self):
        if len(self.drawn_pixels[-1]) == 40:
            self.drawn_pixels.append('')

        if abs(self.sprite_position - self.ray_position) <= 1:
            self.drawn_pixels[-1] += "#"
        else:
            self.drawn_pixels[-1] += " "

    @property
    def ray_position(self):
        return (self.started_cycle - 1) % 40


def part1():
    lines = readlines(FILENAME)

    register = Register()

    for line in lines:
        cleaned_line = line.replace('\n', '')
        register(cleaned_line)

    return sum(register.history)


def part2():
    lines = readlines(FILENAME)

    crt = CRT()

    for line in lines:
        cleaned_line = line.replace('\n', '')
        crt(cleaned_line)

    return crt.drawn_pixels


if __name__ == '__main__':
    print("Advent of Code 2022 Day 10")
    print(f"Part 1: {part1()}")

    print("Part 2")
    print("\n".join(part2()))
