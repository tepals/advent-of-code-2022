def part1(data: str) -> int:
    for i in range(4, len(data) + 1):
        msg = data[i - 4:i]
        if len(set(msg)) == len(msg):
            break
    print(msg)
    return i


def part2(data: str) -> int:
    for i in range(14, len(data) + 1):
        msg = data[i - 14:i]
        if len(set(msg)) == len(msg):
            break
    print(msg)
    return i


if __name__ == '__main__':
    data = open('data-day6.txt', 'r').read()
    print(data)
    print("")
    result_part1 = part1(data)
    print(f"result_part1={result_part1}")
    result_part2 = part2(data)
    print(f"result_part2={result_part2}")
