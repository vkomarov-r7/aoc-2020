from aoc.input import open_input


ccw_rotations = {
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
    (0, -1): (1, 0),
}
cw_rotations = {
    v: k for k, v in ccw_rotations.items()
}

"""
CCW:
-1, 2
-2, -1 (swap, negate row)
1, -2, (swap, negate row)
2, 1, (swap, negate row)
-1, 2 (swap, negate row)

CW:
-1, 2 (swap, negate col)
2, 1, (swap, negate col)
1, -2, (swap, negate col)
-2, -1 (swap, negate col)
-1, 2
"""


def read_instructions():
    instructions = []
    for line in open_input('12.txt'):
        action, value = line[0], line[1:]
        value = int(value)
        instructions.append((action, value))

    return instructions


def part_1():
    loc = [0, 0]
    direction = (0, 1)
    instructions = read_instructions()

    for action, value in instructions:
        if action == 'N':
            loc[0] -= value
        elif action == 'S':
            loc[0] += value
        elif action == 'E':
            loc[1] += value
        elif action == 'W':
            loc[1] -= value
        elif action == 'L':
            assert value % 90 == 0
            for _ in range(value // 90):
                direction = ccw_rotations[direction]
        elif action == 'R':
            assert value % 90 == 0
            for _ in range(value // 90):
                direction = cw_rotations[direction]
        elif action == 'F':
            d_row = direction[0] * value
            d_col = direction[1] * value
            loc[0] += d_row
            loc[1] += d_col
        else:
            raise ValueError(action)

    manhattan_distance = abs(loc[0]) + abs(loc[1])
    print(f"Distance is: {loc[0]} + {loc[1]} = {manhattan_distance}")


def rotate(row, col, dir):
    new_row, new_col = col, row
    if dir == 'L':
        new_row = -new_row
    elif dir == 'R':
        new_col = -new_col
    else:
        raise ValueError(dir)
    return [new_row, new_col]


def part_2():
    loc = [0, 0]
    waypoint = [-1, 10]
    instructions = read_instructions()

    for action, value in instructions:
        if action == 'N':
            waypoint[0] -= value
        elif action == 'S':
            waypoint[0] += value
        elif action == 'E':
            waypoint[1] += value
        elif action == 'W':
            waypoint[1] -= value
        elif action == 'L':
            assert value % 90 == 0
            for _ in range(value // 90):
                waypoint = rotate(waypoint[0], waypoint[1], action)
        elif action == 'R':
            assert value % 90 == 0
            for _ in range(value // 90):
                waypoint = rotate(waypoint[0], waypoint[1], action)
        elif action == 'F':
            d_row = waypoint[0] * value
            d_col = waypoint[1] * value
            loc[0] += d_row
            loc[1] += d_col
        else:
            raise ValueError(action)

    manhattan_distance = abs(loc[0]) + abs(loc[1])
    print(f"Distance is: {loc[0]} + {loc[1]} = {manhattan_distance}")


part_1()
part_2()
