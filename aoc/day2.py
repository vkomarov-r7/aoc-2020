from aoc.input import open_input
import re

REGEX = re.compile(r'(\d+)-(\d+) ([a-z]): (.*)')


def part_1():
    n_valid = 0
    for line in open_input('2.txt'):
        low, high, letter, input = REGEX.match(line).groups()
        low, high = int(low), int(high)
        if low <= input.count(letter) <= high:
            n_valid += 1

    print("Number of valid passwords:", n_valid)


def part_2():
    n_valid = 0
    for line in open_input('2.txt'):
        p1, p2, letter, input = REGEX.match(line).groups()
        p1, p2 = int(p1), int(p2)
        valid = 'NO '

        in_p1 = input[p1 - 1] == letter
        in_p2 = input[p2 - 1] == letter
        if in_p1 != in_p2:
            n_valid += 1
            valid = 'YES'
        print(valid, line.strip())

    print("Number of valid passwords:", n_valid)

part_1()
part_2()
