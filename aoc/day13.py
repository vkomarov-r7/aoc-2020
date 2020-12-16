from aoc.input import open_input
import math


def read_schedule(include_any=False):
    with open_input('13.txt') as fin:
        min_depart_ts = int(fin.readline())
        schedule = []
        for bus in fin.readline().split(','):
            if bus == 'x':
                if include_any:
                    schedule.append(bus)
                else:
                    continue
            else:
                schedule.append(int(bus))
    return min_depart_ts, schedule


def part_1():
    min_depart_ts, schedule = read_schedule()

    print(min_depart_ts, schedule)

    options = []
    for bus_n in schedule:
        wait = bus_n - (min_depart_ts % bus_n)
        options.append((wait, bus_n))

    wait, bus_n = sorted(options, key=lambda entry: entry[0])[0]
    print(f"Found earliest bus: {bus_n}, waiting for {wait}: {wait * bus_n}")


def part_2_brute():
    # This doesn't work.
    _, schedule = read_schedule(include_any=True)
    print(schedule)

    ts = 100000000000000
    while True:
        found = False
        # print("Evaluating ts", ts)
        for d_t, bus_n in enumerate(schedule):
            # if ts == 1068781:
            #     breakpoint()
            # print("Evaluating bus", bus_n)
            if bus_n == 'x':
                # print("skipping unknown bus", d_t)
                continue

            departs_now = ((ts + d_t) % bus_n) == 0
            if not departs_now:
                # print(f"Departure time is incorrect {d_t}, {bus_n}, expected: {d_t}")
                break
        else:
            print("Found it!", ts, d_t, bus_n)
            found = True

        if found:
            break

        ts += schedule[0]
    print("Found best timestamp", ts + schedule[0])


def part_2():
    _, schedule = read_schedule(include_any=True)
    print(schedule)

    ts = 0
    increment = 1

    for d_ts, bus_n in enumerate(schedule):
        if bus_n == 'x':
            continue

        # keep bumping by the increment until we hit the next bus schedule.
        while (ts + d_ts) % bus_n != 0:
            ts += increment

        # won't see any more collisions for at least this much.
        increment *= bus_n

    print("Ideal solution", ts)


part_1()
part_2()
