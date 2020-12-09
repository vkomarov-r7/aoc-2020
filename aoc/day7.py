import re
from aoc.input import open_input


def read_bag(description):
    source_color, contents = re.match(r'(.+) bags contain (.*)\.', description).groups()
    parsed_contents = {}
    for content in contents.split(', '):
        if content == 'no other bags':
            break
        n, color = re.match(r'(\d+) (.+) bags?', content).groups()
        n = int(n)
        parsed_contents[color] = n
    return source_color, parsed_contents


def read_bags():
    bags = {}
    for line in open_input('7.txt'):
        color, contents = read_bag(line)
        bags[color] = contents
    return bags


def reverse_contents(bag):
    reversed_contents = {}
    for color, contents in bag.items():
        for contained_color in contents.keys():
            reversed_contents.setdefault(contained_color, set()).add(color)
    return reversed_contents


def part_1():
    bags = read_bags()
    reversed_contents = reverse_contents(bags)

    q = ['shiny gold']
    seen = set()
    while q:
        color = q.pop()
        if color in seen:
            continue

        seen.add(color)
        q.extend(reversed_contents.get(color, []))

    print("Total bag colors that can contain shiny gold:", len(seen) - 1)


def multiply_contents(contents, quantity):
    new_contents = {}
    for color, n in contents.items():
        new_contents[color] = n * quantity
    return new_contents


def merge_contents(a, b):
    new_contents = {}
    for color, n, in a.items():
        existing_n = new_contents.get(color, 0)
        new_contents[color] = existing_n + n

    for color, n, in b.items():
        existing_n = new_contents.get(color, 0)
        new_contents[color] = existing_n + n

    return new_contents


def part_2():
    bags = read_bags()
    count = 0  # shiny gold bag
    contents = bags['shiny gold']
    while contents:
        color = next(iter(sorted(contents.keys())))
        quantity = contents.pop(color)
        count += quantity
        new_contents = multiply_contents(bags[color], quantity)
        contents = merge_contents(contents, new_contents)
    print("Total count required:", count)


part_1()
part_2()
