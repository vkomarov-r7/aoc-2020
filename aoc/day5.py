from aoc.input import open_input


def get_seat_id(instructions):
    row_min, row_max = 0, 127
    col_min, col_max = 0, 7
    for instruction in instructions:
        if instruction == 'F':
            row_max = (row_min + row_max) // 2
        elif instruction == 'B':
            row_min = (row_min + row_max + 1) // 2
        elif instruction == 'L':
            col_max = (col_min + col_max) // 2
        elif instruction == 'R':
            col_min = (col_min + col_max + 1) // 2
        elif instruction == '\n':
            continue
        else:
            raise ValueError(instruction)
    assert row_min == row_max
    assert col_min == col_max

    seat_id = row_min * 8 + col_min
    return seat_id


def part_1():
    example_seat_id = get_seat_id('FBFBBFFRLR')  # example
    print("Example seat_id:", example_seat_id)

    max_seat_id = max(
        get_seat_id(instructions)
        for instructions in open_input('5.txt')
    )
    print("Max seat_id:", max_seat_id)


def part_2():
    seat_ids = sorted(
        get_seat_id(instructions)
        for instructions in open_input('5.txt')
    )

    prev_seat_id = seat_ids[0]
    for seat_id in seat_ids[1:]:
        delta = seat_id - prev_seat_id
        prev_seat_id = seat_id
        if delta != 1:
            print("Found our seat:", seat_id - 1)
            return


part_1()
part_2()
