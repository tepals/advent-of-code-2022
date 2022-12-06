
def part1(data):
    pairs = 0
    for row in data:
        left, right = [[int(j) for j in i.split("-")] for i in row.split(",")]
        overlap = set(range(left[0], left[1] + 1)) & set(range(right[0], right[1] + 1))
        if set(left) & overlap == set(left) or set(right) & overlap == set(right):
            pairs += 1
    return pairs


def part2(data):
    pairs = 0
    for row in data:
        left, right = [[int(j) for j in i.split("-")] for i in row.split(",")]
        overlap = set(range(left[0], left[1] + 1)) & set(range(right[0], right[1] + 1))
        if overlap:
            pairs += 1
    return pairs


if __name__ == '__main__':
    data = open('data-day4.txt', 'r').read()
    total_part1 = part1(data.split("\n"))
    print(f"total_part1={total_part1}")
    total_part2 = part2(data.split("\n"))
    print(f"total_part2={total_part2}")
