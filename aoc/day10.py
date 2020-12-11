from aoc.input import open_input


def read_adapters():
    adapters = set()
    for line in open_input('10.txt'):
        adapter = int(line)
        adapters.add(adapter)
    return adapters


def part_1():
    adapters = read_adapters()
    cur_jolt = 0
    differences = {1: 0, 2: 0, 3: 1}

    while cur_jolt != max(adapters):
        for difference in range(1, 4):
            possible_jolt = cur_jolt + difference
            if possible_jolt in adapters:
                cur_jolt = possible_jolt
                differences[difference] += 1
                break

    one_jolt_diff = differences[1]
    three_jolt_diff = differences[3]
    combined = one_jolt_diff * three_jolt_diff
    print(f"Multiplied differences: {one_jolt_diff} * {three_jolt_diff} = {combined}")


def part_2():
    adapters = read_adapters()
    cur_jolt = 0
    jolt_possibilities = {adapter: 0 for adapter in sorted(adapters)}
    jolt_possibilities[0] = 1

    while cur_jolt != max(adapters):
        next_jolt = None
        for difference in range(1, 4):
            possible_jolt = cur_jolt + difference
            if possible_jolt in adapters:
                if not next_jolt:
                    next_jolt = possible_jolt
                jolt_possibilities[possible_jolt] += jolt_possibilities[cur_jolt]
        cur_jolt = next_jolt

    total_possibilities = jolt_possibilities[max(adapters)]
    print("Total possibilities:", total_possibilities)


part_1()
part_2()
