from aoc.input import open_input


PREAMBLE_LEN = 25


def read_numbers():
    numbers = []
    for line in open_input('9.txt'):
        num = int(line)
        numbers.append(num)
    return numbers


def part_1():
    numbers = read_numbers()
    preamble_l = numbers[:PREAMBLE_LEN]
    preamble_s = set(numbers[:PREAMBLE_LEN])
    outgoing = preamble_l[0]

    for new_num in numbers[PREAMBLE_LEN:]:
        print("investigating number", new_num)
        valid = False
        for preamble_num in preamble_l:
            difference = new_num - preamble_num
            if difference in preamble_s and difference != preamble_num:
                valid = True
                break

        if not valid:
            print("Invalid number in code:", new_num)
            return

        preamble_s.remove(outgoing)
        preamble_s.add(new_num)
        preamble_l.append(new_num)
        preamble_l = preamble_l[1:]
        outgoing = preamble_l[0]


def part_2():
    numbers = read_numbers()
    target_sum = 20874512  # output from part 1
    rolling_sum = numbers[0]
    low_idx = 0
    high_idx = 0

    while rolling_sum != target_sum:
        if rolling_sum > target_sum:
            rolling_sum -= numbers[low_idx]
            low_idx += 1
        elif rolling_sum < target_sum:
            high_idx += 1
            rolling_sum += numbers[high_idx]
        else:
            raise ValueError('It is equal?')

    sublist = numbers[low_idx:high_idx + 1]
    weak_num = min(sublist) + max(sublist)
    print("Weak number is", weak_num)


part_1()
part_2()
