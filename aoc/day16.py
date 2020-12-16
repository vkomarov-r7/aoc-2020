from aoc.input import open_input


class Interval:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def contains(self, n):
        return l <= n <= r

    def repr(self):
        return f"Interval({l}-{r})"


def read_tickets():
    constraints = {}
    ticket = []
    nearby_tickets = []
    with open_input('16.txt') as fin:
        while True:
            line = fin.readline().strip()
            if not line:
                break

            name, constraint_str = line.split(':')
            parsed_constraints = []
            for constraint in constraint_str.split(' or '):
                l, r = constraint.split('-')
                parsed_constraints.append((int(l), int(r)))

            constraints[name] = parsed_constraints

        fin.readline()  # your ticket:
        ticket = [int(n) for n in fin.readline().split(',')]

        fin.readline() # \n
        fin.readline() # nearby tickets
        for line in fin:
            nearby_ticket = [int(n) for n in line.split(',')]
            nearby_tickets.append(nearby_ticket)

    return constraints, ticket, nearby_tickets


def matches_constraints(n, constraints):
    for constraint in constraints:
        if constraint[0] <= n <= constraint[1]:
            return True
    return False


def part_1():
    constraints, ticket, nearby_tickets = read_tickets()
    print("Constraints", constraints)
    print("Ticket", ticket)
    print("Nearby Tickets", nearby_tickets)

    invalid_nums = []
    for nearby_ticket in nearby_tickets:
        for n in nearby_ticket:
            valid = False
            for constraint in constraints.values():
                if matches_constraints(n, constraint):
                    valid = True
                    break

            if not valid:
                invalid_nums.append(n)
                break

    total = 0
    for n in invalid_nums:
        total += n
    print("Sum of invalid numbers", total)


def is_valid_ticket(ticket, all_constraints):
    for n in ticket:
        valid = False
        for constraint in all_constraints.values():
            if matches_constraints(n, constraint):
                valid = True
                break

        if not valid:
            return False
    return True


def part_2():
    constraints, my_ticket, nearby_tickets = read_tickets()
    print("Constraints", constraints)
    print("Ticket", my_ticket)
    print("Nearby Tickets", nearby_tickets)

    invalid_nums = []
    nearby_tickets = [
        ticket
        for ticket in nearby_tickets
        if is_valid_ticket(ticket, constraints)
    ]

    constraint_possibilities = {
        c: list(range(len(my_ticket)))
        for c in constraints
    }

    for ticket in nearby_tickets:
        for idx, n in enumerate(ticket):
            for constraint_name, constraint in constraints.items():
                if idx in constraint_possibilities[constraint_name] and not matches_constraints(n, constraint):
                    constraint_possibilities[constraint_name].remove(idx)

    locked_constraints = set()
    while len(locked_constraints) != len(constraints):
        for name, positions in constraint_possibilities.items():
            if name in locked_constraints:
                continue

            if len(positions) == 1:
                locked_constraints.add(name)
                position = positions[0]
                for n, ps in constraint_possibilities.items():
                    if name != n and position in ps:
                        ps.remove(position)

    print("After locking", constraint_possibilities)
    departure_nums = []
    departure_product = 1
    for name, pos in constraint_possibilities.items():
        if name.startswith('departure'):
            print("Departure number", name, pos[0], my_ticket[pos[0]])
            departure_product *= my_ticket[pos[0]]

    print("Departure product", departure_product)


part_1()
part_2()
