from utils.day02 import parse_left_move, parse_right_move
from utils.day02 import parse_right_outcome
from utils.day02 import move_score, outcome_score

from utils.utils import readlines


FILENAME = 'data/day02.txt'

outcome_table = {"Rock": {"Rock": "Tie", "Paper": "Lose", "Scissors": "Win"},
                 "Paper": {"Rock": "Win", "Paper": "Tie", "Scissors": "Lose"},
                 "Scissors": {"Rock": "Lose", "Paper": "Win", "Scissors": "Tie"}}

move_table = {"Rock": {"Tie": "Rock", "Win": "Paper", "Lose": "Scissors"},
              "Paper": {"Lose": "Rock", "Tie": "Paper", "Win": "Scissors"},
              "Scissors": {"Win": "Rock", "Lose": "Paper", "Tie": "Scissors"}}


def part1():
    lines = readlines(FILENAME)

    total = 0

    for line in lines:
        cleaned_line = line.replace('\n', '')

        left_move, right_move = cleaned_line.split(" ")

        left_move = parse_left_move(left_move)
        right_move = parse_right_move(right_move)

        outcome = outcome_table[right_move][left_move]

        score = outcome_score(outcome) + move_score(right_move)

        total += score

    return total


def part2():
    lines = readlines(FILENAME)

    total = 0

    for line in lines:
        cleaned_line = line.replace('\n', '')

        left_move, right_outcome = cleaned_line.split(" ")

        left_move = parse_left_move(left_move)
        outcome = parse_right_outcome(right_outcome)

        right_move = move_table[left_move][outcome]

        score = outcome_score(outcome) + move_score(right_move)

        total += score

    return total


if __name__ == '__main__':
    print("Advent of Code 2022 Day 02")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
