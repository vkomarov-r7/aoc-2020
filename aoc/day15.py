from collections import defaultdict
from aoc.input import open_input


def read_starting():
    numbers = []
    for item in open_input('15.txt').readline().split(','):
        numbers.append(int(item))
    return numbers


def part_1():
    turns_spoken = defaultdict(list)
    numbers = read_starting()

    # process starting numbers
    for turn, n in enumerate(numbers):
        turns_spoken[n].append(turn + 1)
    # print(turns_spoken)

    last = numbers[-1]
    for turn in range(len(numbers) + 1, 2021):
        new_n = 0
        if len(turns_spoken[last]) > 1:
            new_n = turns_spoken[last][0] - turns_spoken[last][1]

        turns_spoken[new_n].insert(0, turn)
        turns_spoken[new_n] = turns_spoken[new_n][:2]
        print(f"Turn: {turn}, the number is: {new_n}")
        last = new_n

    print(f"Final turn: {turn}, final number: {new_n}")


def part_2():
    turns_spoken = defaultdict(list)
    numbers = read_starting()

    # process starting numbers
    for turn, n in enumerate(numbers):
        turns_spoken[n].append(turn + 1)
    # print(turns_spoken)

    last = numbers[-1]
    for turn in range(len(numbers) + 1, 30000001):
        if turn % 100000 == 0:
            print("Current turn", turn)
        new_n = 0
        if len(turns_spoken[last]) > 1:
            new_n = turns_spoken[last][0] - turns_spoken[last][1]

        turns_spoken[new_n].insert(0, turn)
        turns_spoken[new_n] = turns_spoken[new_n][:2]
        # print(f"Turn: {turn}, the number is: {new_n}")
        last = new_n

    print(f"Final turn: {turn}, final number: {new_n}")

part_1()
part_2()
