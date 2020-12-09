import math
from aoc.input import open_input


def load_map():
    map = []
    for line in open_input('3.txt'):
        row = list(line.strip())
        map.append(row)
    return map


def part_1():
    map = load_map()
    row_len = len(map)
    col_len = len(map[0])

    row, col = 0, 0
    n_trees = 0
    while row < len(map):
        row += 1
        col += 3
        if map[row % row_len][col % col_len] == '#':
            n_trees += 1

    print("Total trees encountered:", n_trees)


def count_trees(map, row_offset, col_offset):
    row_len = len(map)
    col_len = len(map[0])

    row, col = 0, 0
    n_trees = 0
    while row < len(map):
        row += row_offset
        col += col_offset
        if map[row % row_len][col % col_len] == '#':
            n_trees += 1
    return n_trees


def part_2():
    offsets = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 1),
    ]
    map = load_map()
    tree_counts = [count_trees(map, *offset) for offset in offsets]
    total = 1
    for cnt in tree_counts:
        total *= cnt
    print(f"Tree counts: {tree_counts}, total: {total}")


part_1()
part_2()
