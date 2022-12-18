from functools import reduce

from utils.utils import readlines

FILENAME = 'data/day11.txt'


class Monkey:
    def __init__(self, attributes):
        self._parse_monkey_attributes(attributes)
        self.inspected_items = 0

    def _parse_monkey_attributes(self, attributes):
        monkey_name, starting_items, operation, test, if_true, if_false = attributes

        self.name = int(monkey_name[7:-1])

        self.items = [int(x) for x in starting_items[18:].split(',')]

        left_operand, operator, right_operand = operation[19:].split(' ')
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

        self.M = int(test[21:])

        self.if_true_monkey = int(if_true[29:])
        self.if_false_monkey = int(if_false[30:])

    def update_item_worry_level(self, worry_level):
        left_val = worry_level if self.left_operand == 'old' else int(self.left_operand)
        right_val = worry_level if self.right_operand == 'old' else int(self.right_operand)

        return self._compute(self.operator, left_val, right_val) // 3

    @staticmethod
    def _compute(operator, left_val, right_val):
        # There is an easier way to do this by using the os module, but na
        if operator == '-':
            return left_val - right_val
        elif operator == '+':
            return left_val + right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
        raise ValueError(f"{operator} not understood.")

    def __repr__(self):
        return f"Monkey {self.name}"


class Troop:
    def __init__(self, monkey_attributes):
        monkeys = [Monkey(attributes) for attributes in monkey_attributes]
        self.monkeys = {monkey.name: monkey for monkey in monkeys}

    def update_troop(self, N=1):
        for _ in range(N):
            self._update_troop()

    def _update_troop(self):
        for i in range(len(self.monkeys)):
            self._update_monkey(i)

    def _update_monkey(self, i):
        current_monkey = self.monkeys[i]
        self._update_monkey_items_worry_level(current_monkey)

        if_true_monkey = self.monkeys[current_monkey.if_true_monkey]
        if_false_monkey = self.monkeys[current_monkey.if_false_monkey]

        for worry_level in current_monkey.items:
            if worry_level % current_monkey.M == 0:
                if_true_monkey.items.append(worry_level)
            else:
                if_false_monkey.items.append(worry_level)

        current_monkey.items = []

    @staticmethod
    def _update_monkey_items_worry_level(monkey):
        for i, worry_level in enumerate(monkey.items):
            new_val = monkey.update_item_worry_level(worry_level)
            monkey.items[i] = new_val

            monkey.inspected_items += 1

    @staticmethod
    def _compute(operator, left_val, right_val):
        # There is an easier way to do this by using the os module, but na
        if operator == '-':
            return left_val - right_val
        elif operator == '+':
            return left_val + right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
        raise ValueError(f"{operator} not understood.")


class MonkeyV2:
    def __init__(self, attributes):
        self._parse_monkey_attributes(attributes)
        self.inspected_items = 0

    def _parse_monkey_attributes(self, attributes):
        monkey_name, starting_items, operation, test, if_true, if_false = attributes

        self.name = int(monkey_name[7:-1])

        self.items = [int(x) for x in starting_items[18:].split(',')]

        left_operand, operator, right_operand = operation[19:].split(' ')
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

        self.M = int(test[21:])

        self.if_true_monkey = int(if_true[29:])
        self.if_false_monkey = int(if_false[30:])

    def update_item_worry_level(self, worry_level, N):
        left_val = worry_level if self.left_operand == 'old' else int(self.left_operand)
        right_val = worry_level if self.right_operand == 'old' else int(self.right_operand)

        return self._compute(self.operator, left_val, right_val) % N

    @staticmethod
    def _compute(operator, left_val, right_val):
        # There is an easier way to do this by using the os module, but na
        if operator == '-':
            return left_val - right_val
        elif operator == '+':
            return left_val + right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
        raise ValueError(f"{operator} not understood.")

    def __repr__(self):
        return f"Monkey {self.name}"
class TroopV2:
    def __init__(self, monkey_attributes):
        monkeys = [MonkeyV2(attributes) for attributes in monkey_attributes]
        self.monkeys = {monkey.name: monkey for monkey in monkeys}

        self.N = reduce(lambda x, y: x * y,
                        [monkey.M for monkey in self.monkeys.values()], 1)

    def update_troop(self, N=1):
        for _ in range(N):
            self._update_troop()

    def _update_troop(self):
        for i in range(len(self.monkeys)):
            self._update_monkey(i)

    def _update_monkey(self, i):
        current_monkey = self.monkeys[i]
        self._update_monkey_items_worry_level(current_monkey, self.N)

        if_true_monkey = self.monkeys[current_monkey.if_true_monkey]
        if_false_monkey = self.monkeys[current_monkey.if_false_monkey]

        for worry_level in current_monkey.items:
            if worry_level % current_monkey.M == 0:
                if_true_monkey.items.append(worry_level)
            else:
                if_false_monkey.items.append(worry_level)

        current_monkey.items = []

    @staticmethod
    def _update_monkey_items_worry_level(monkey, N):
        for i, worry_level in enumerate(monkey.items):
            new_val = monkey.update_item_worry_level(worry_level, N)
            monkey.items[i] = new_val

            monkey.inspected_items += 1

    @staticmethod
    def _compute(operator, left_val, right_val):
        # There is an easier way to do this by using the os module, but na
        if operator == '-':
            return left_val - right_val
        elif operator == '+':
            return left_val + right_val
        elif operator == '*':
            return left_val * right_val
        elif operator == '/':
            return left_val / right_val
        raise ValueError(f"{operator} not understood.")


def part1():
    lines = readlines(FILENAME)

    i = 0
    monkey_attributes = []

    while i < len(lines):
        monkey_attributes.append([x.replace('\n', '') for x in lines[i: i + 6]])
        i += 7

    troop = Troop(monkey_attributes)

    troop.update_troop(20)

    val1, val2, *vals = sorted([m.inspected_items for m in troop.monkeys.values()], reverse=True)
    return val1 * val2


def part2():
    lines = readlines(FILENAME)

    i = 0
    monkey_attributes = []

    while i < len(lines):
        monkey_attributes.append([x.replace('\n', '') for x in lines[i: i + 6]])
        i += 7

    troop = TroopV2(monkey_attributes)
    troop.update_troop(10_000)

    val1, val2, *vals = sorted([m.inspected_items for m in troop.monkeys.values()], reverse=True)
    return val1 * val2


if __name__ == '__main__':
    print("Advent of Code 2022 Day 11")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
