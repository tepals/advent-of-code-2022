def part1(data):
    data = data.replace("A", "X")
    data = data.replace("B", "Y")
    data = data.replace("C", "Z")
    rounds = data.split("\n")
    points = {"X": 1, "Y": 2, "Z": 3}
    wins = {"X": "Z", "Y": "X", "Z": "Y"}
    total_points = 0
    for round in rounds:
        elf, me = round.split(" ")
        if elf == me:
            total_points += 3
        elif elf == wins[me]:
            total_points += 6
        else:
            total_points += 0
        total_points += points[me]

    print(total_points)
    return total_points


def part2(data):
    rounds = data.split("\n")
    exp_result = {"X": "lose", "Y": "draw", "Z": "win"}
    possible_results = {
        "A": {"lose": 3 + 0, "draw": 1 + 3, "win": 2 + 6},
        "B": {"lose": 1 + 0, "draw": 2 + 3, "win": 3 + 6},
        "C": {"lose": 2 + 0, "draw": 3 + 3, "win": 1 + 6},
    }
    total_points = 0
    for round in rounds:
        elf, result = round.split(" ")
        total_points += possible_results[elf][exp_result[result]]
    print(total_points)
    return total_points


if __name__ == '__main__':
    data = open('data-day2.txt', 'r').read()
    part1(data)
    part2(data)
