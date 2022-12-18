from utils.utils import readlines

FILENAME = 'data/day13.txt'


def compare(left_value, right_value):
    if (not isinstance(left_value, list)) and (not isinstance(right_value, list)):
        if left_value < right_value:
            return True
        elif left_value > right_value:
            return False
        return None

    elif isinstance(left_value, list) and isinstance(right_value, list):
        N = len(left_value)
        for i in range(N):
            if i + 1 > len(right_value):
                return False

            val = compare(left_value[i], right_value[i])
            if val is not None:
                return val

        if len(left_value) < len(right_value):
            return True

        return None
    elif isinstance(left_value, list):
        return compare(left_value, [right_value])

    elif isinstance(right_value, list):
        return compare([left_value], right_value)


def parse_list(l):
    stack = [[]]
    current_char = ''

    for char in l:
        if char == '[':
            stack.append([])
        elif char == ']':
            if current_char != '':
                stack[-1].append(int(current_char))
                current_char = ''

            val = stack.pop()
            stack[-1].append(val)
        elif char == ',':
            if current_char != '':
                stack[-1].append(int(current_char))
                current_char = ''
        else:
            current_char += char

    return stack[0][0]


def binary_sort(packets):
    if len(packets) == 1 or len(packets) == 0:
        return packets

    pivot = packets[0]

    left_of_pivot = []
    right_of_pivot = []

    for packet in packets[1:]:
        if not compare(pivot, packet):
            left_of_pivot.append(packet)
        else:
            right_of_pivot.append(packet)

    return binary_sort(left_of_pivot) + [pivot] + binary_sort(right_of_pivot)


def part1():
    lines = readlines(FILENAME)

    cleaned_lines = [line.replace('\n', '') for line in lines]

    packets = []
    for left_value, right_value in zip(cleaned_lines[::3], cleaned_lines[1::3]):
        packets.append(parse_list(left_value))
        packets.append(parse_list(right_value))

    counter = 0

    for i, (left_value, right_value) in enumerate(zip(cleaned_lines[::3], cleaned_lines[1::3])):
        val = compare(parse_list(left_value), parse_list(right_value))
        counter += (i + 1) * val

    return counter


def part2():
    lines = readlines(FILENAME)

    cleaned_lines = [line.replace('\n', '') for line in lines]

    packets = []
    for left_value, right_value in zip(cleaned_lines[::3], cleaned_lines[1::3]):
        packets.append(parse_list(left_value))
        packets.append(parse_list(right_value))

    packets.append([[2]])
    packets.append([[6]])

    counter = 1

    sorted_packets = binary_sort(packets)
    for i, packet in enumerate(sorted_packets):
        if packet == [[2]] or packet == [[6]]:
            counter *= i + 1

    return counter


if __name__ == '__main__':
    print("Advent of Code 2022 Day 13")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
