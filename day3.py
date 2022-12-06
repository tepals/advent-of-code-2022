import math


def get_priority(itm):
    if itm.lower() == itm:
        prio = ord(itm) - 96
    else:
        prio = ord(itm) - 38
    return prio


def part1(data):
    total = 0
    for row in data:
        left = row[:int(len(row) / 2)]
        right = row[int(len(row) / 2):]
        common_item = set(left).intersection(set(right)).pop()
        total += get_priority(common_item)
    return total


def part2(data):
    n = 3
    total = 0
    for i in range(math.ceil(len(data) / 3)):
        common_item = set(data[n-3]) & set(data[n-2]) & set(data[n-1])
        total += get_priority(common_item.pop())
        n += 3
    return total


if __name__ == '__main__':
    data = open('data-day3.txt', 'r').read()
    total_part1 = part1(data.split("\n"))
    print(f"total_part1={total_part1}")
    total_part2 = part2(data.split("\n"))
    print(f"total_part2={total_part2}")
