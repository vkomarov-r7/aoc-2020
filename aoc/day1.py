from aoc.input import open_input


def part_1():
    numbers = [int(l) for l in open_input('1.txt')]

    for idx, x in enumerate(numbers):
        for y in numbers[idx+1:]:
            if x + y == 2020:
                print(f"Found {x} * {y}: {x * y}")


def part_2():
    numbers = [int(l) for l in open_input('1.txt')]

    for idx, x in enumerate(numbers):
        for idx_2, y in enumerate(numbers[idx+1:]):
            for z in numbers[idx_2+1:]:
                if x + y + z == 2020:
                    print(f"Found {x} * {y} * {z}: {x * y * z}")

part_1()
part_2()
