from aoc.input import open_input


def part_1_read_groups():
    group = set()
    for line in open_input('6.txt'):
        line = line.strip()
        if not line:
            yield group
            group = set()
        group.update(line)

    yield group


def part_1():
    groups = part_1_read_groups()
    counts = sum(len(group) for group in groups)
    print("Total counts (part 1):", counts)


def part_2_read_groups():
    group = set('abcdefghijklmnopqrstuvwxyz')
    for line in open_input('6.txt'):
        line = line.strip()
        if not line:
            yield group
            group = set('abcdefghijklmnopqrstuvwxyz')
            continue
        group = group.intersection(line)

    yield group


def part_2():
    groups = part_2_read_groups()
    counts = sum(len(group) for group in groups)
    print("Total counts (part 2):", counts)


part_1()
part_2()
