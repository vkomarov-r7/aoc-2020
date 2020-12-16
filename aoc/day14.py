from aoc.input import open_input

def bits_to_value(bits):
    value = 0
    for n, bit in enumerate(bits):
        if bit:
            value += 2 ** (35 - n)
    return value


def value_to_bits(value):
    bits = [0 for _ in range(36)]
    n = 35
    while value:
        bit = value % 2
        bits[n] = bit
        value //= 2
        n -= 1
    return bits


def parse_mask(line):
    mask_idx = line.index('=') + 2
    mask = []

    for chr in line[mask_idx:]:
        if chr == 'X':
            mask.append(None)
        else:
            mask.append(int(chr))
    return mask


def apply_mask(value, mask):
    new_value = []

    for n in range(len(value)):
        v = value[n]
        m = mask[n]

        if m is not None:
            v = m

        new_value.append(v)
    return new_value



def parse_memset(line):
    l_off = line.index('[') + 1
    r_off = line.index(']')
    value_off = line.index('=') + 2

    addr = int(line[l_off:r_off])
    value = int(line[value_off:])
    return addr, value


def part_1():
    mask = [0 for _ in range(36)]
    memory = {}
    for line in open_input('14.txt'):
        line = line.strip()
        if line.startswith('mask'):
            mask = parse_mask(line)
        elif line.startswith('mem'):
            addr, value = parse_memset(line)
            value = apply_mask(value_to_bits(value), mask)
            memory[addr] = bits_to_value(value)

    total = 0
    for value in memory.values():
        total += value

    print("The final value is:", total)


def get_addr_perms(addr, mask):
    all_addrs = [[]]

    def add_char(c):
        for addr in all_addrs:
            addr.append(c)

    for n in range(len(addr)):
        a = addr[n]
        m = mask[n]

        if m == 1:
            add_char(1)
        elif m == 0:
            add_char(a)
        elif m is None:
            new_addrs = []
            for existing_addr in all_addrs:
                new_addrs.append(existing_addr + [0])
                new_addrs.append(existing_addr + [1])
            all_addrs = new_addrs

    return all_addrs


def part_2():
    mask = [0 for _ in range(36)]
    memory = {}
    for line in open_input('14.txt'):
        line = line.strip()
        if line.startswith('mask'):
            mask = parse_mask(line)
        elif line.startswith('mem'):
            addr, value = parse_memset(line)
            addr_bits = value_to_bits(addr)
            for new_addr in get_addr_perms(addr_bits, mask):
                memory[bits_to_value(new_addr)] = value

    total = 0
    for value in memory.values():
        total += value

    print("The final value is:", total)


# part_1()
part_2()
