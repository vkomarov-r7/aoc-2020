from aoc.input import open_input
from copy import deepcopy


OFFSETS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def read_seats():
    seats = []
    for line in open_input('11.txt'):
        line = line.strip()
        seats.append(list(line))
    return seats


def adjacents(seats, row, col):
    max_row = len(seats) - 1
    max_col = len(seats[0]) - 1
    adjacent_seats = []

    for d_row, d_col in OFFSETS:
        new_row, new_col = row + d_row, col + d_col

        if new_row < 0 or new_row > max_row:
            continue
        if new_col < 0 or new_col > max_col:
            continue

        seat = seats[new_row][new_col]
        adjacent_seats.append(seat)

    return adjacent_seats


def one_round(seats):
    new_seats = deepcopy(seats)
    any_changes = False


    for row_n in range(len(seats)):
        for col_n in range(len(seats[0])):
            adj = adjacents(seats, row_n, col_n)
            seat = seats[row_n][col_n]

            occupied_count = adj.count('#')
            if seat == 'L' and adj.count('#') == 0:
                new_seats[row_n][col_n] = '#'
                any_changes = True
            if seat == '#' and occupied_count >= 4:
                new_seats[row_n][col_n] = 'L'
                any_changes = True

    return any_changes, new_seats


def print_seats(seats):
    print()
    print('------ Seats -------')
    for row in seats:
        print(''.join(row))


def count_by_type(seats, seat_type):
    total_count = 0
    for row in seats:
        total_count += row.count(seat_type)
    return total_count


def part_1():
    seats = read_seats()

    any_changes = True
    while any_changes:
        any_changes, seats = one_round(seats)

    total_occupied = count_by_type(seats, '#')
    print("Total occupied seats is:", total_occupied)


def seen_adjacents(seats, row, col):
    max_row = len(seats) - 1
    max_col = len(seats[0]) - 1

    def is_in_range(r, c):
        if r < 0 or r > max_row:
            return False
        if c < 0 or c > max_col:
            return False
        return True

    adjacent_seats = []

    for d_row, d_col in OFFSETS:
        seen_seat = '.'

        new_row, new_col = row + d_row, col + d_col
        while seen_seat == '.' and is_in_range(new_row, new_col):
            seen_seat = seats[new_row][new_col]
            new_row, new_col = new_row + d_row, new_col + d_col

        if seen_seat != '.':
            adjacent_seats.append(seen_seat)

    return adjacent_seats


def one_round(seats):
    new_seats = deepcopy(seats)
    any_changes = False

    for row_n in range(len(seats)):
        for col_n in range(len(seats[0])):
            adj = seen_adjacents(seats, row_n, col_n)
            seat = seats[row_n][col_n]

            occupied_count = adj.count('#')
            if seat == 'L' and adj.count('#') == 0:
                new_seats[row_n][col_n] = '#'
                any_changes = True
            if seat == '#' and occupied_count >= 5:
                new_seats[row_n][col_n] = 'L'
                any_changes = True

    return any_changes, new_seats

def part_2():
    # seats = read_seats()
    # seen
    # return
    seats = read_seats()

    any_changes = True
    while any_changes:
        any_changes, seats = one_round(seats)

    total_occupied = count_by_type(seats, '#')
    print("Total occupied seats is:", total_occupied)


part_1()
part_2()
