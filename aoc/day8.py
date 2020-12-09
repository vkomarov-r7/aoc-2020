from aoc.input import open_input
from copy import deepcopy

class InfiniteLoopError(Exception):
    pass


def read_instructions():
    instructions = []
    for line in open_input('8.txt'):
        line = line.strip()
        if not line:
            continue
        instruction, offset = line.split(' ')
        offset = int(offset)
        instructions.append((instruction, offset))
    return instructions


def part_1():
    instructions = read_instructions()
    executed = set()
    registers = {
        'pc': 0,
        'acc': 0,
    }

    while True:
        pc = registers['pc']
        if pc in executed:
            print("Accumulator value is:", registers['acc'])
            return
        executed.add(pc)
        instruction, offset = instructions[pc]
        pc_offset = 1
        if instruction == 'acc':
            registers['acc'] += offset
        elif instruction == 'nop':
            pass
        elif instruction == 'jmp':
            pc_offset = offset
        else:
            raise ValueError(instruction)
        registers['pc'] += pc_offset


def run_computer(instructions):
    executed = set()
    registers = {
        'pc': 0,
        'acc': 0,
    }

    while registers['pc'] < len(instructions):
        pc = registers['pc']
        if pc in executed:
            raise InfiniteLoopError
        executed.add(pc)
        instruction, offset = instructions[pc]
        pc_offset = 1
        if instruction == 'acc':
            registers['acc'] += offset
        elif instruction == 'nop':
            pass
        elif instruction == 'jmp':
            pc_offset = offset
        else:
            raise ValueError(instruction)
        registers['pc'] += pc_offset
    return registers


def part_2():
    instructions = read_instructions()
    for idx, (cmd, offset) in enumerate(instructions):
        if cmd in ('nop', 'jmp'):
            swapped_cmd = 'nop' if cmd == 'jmp' else 'jmp'
            instructions[idx] = swapped_cmd, offset
            try:
                registers = run_computer(instructions)
            except InfiniteLoopError:
                # wasn't it, put it back.
                instructions[idx] = cmd, offset
            else:
                print("Accumulator value after swapping:", registers['acc'])
                return


part_1()
part_2()
