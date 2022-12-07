import re

import math


def part1(stacks: str, moves: str) -> str:
    stacks = stacks.split("\n")
    crate_nrs = list(filter(None, stacks[-1].split(" ")))
    crate_dict = get_crate_dict(stacks, crate_nrs)

    for move in moves.split("\n"):
        n_moves, move_from, move_to = split_move(move)
        for i in range(n_moves):
            crate_dict[move_to].append(crate_dict[move_from].pop())

    message = "".join([crate_dict[int(i)][-1] for i in crate_nrs]).replace("[", "").replace("]", "")
    return message


def split_move(move: str) -> tuple:
    result = re.search("move (.*) from (.*) to (.*)", move)
    n_moves = int(result.group(1))
    move_from = int(result.group(2))
    move_to = int(result.group(3))
    return n_moves, move_from, move_to


def part2(stacks: str, moves: str) -> str:
    stacks = stacks.split("\n")
    crate_nrs = list(filter(None, stacks[-1].split(" ")))
    crate_dict = get_crate_dict(stacks, crate_nrs)

    for move in moves.split("\n"):
        n_moves, move_from, move_to = split_move(move)
        crate_dict[move_to].extend(crate_dict[move_from][-n_moves:])
        crate_dict[move_from] = crate_dict[move_from][:-n_moves]

    message = "".join([crate_dict[int(i)][-1] for i in crate_nrs]).replace("[", "").replace("]", "")

    return message


def get_crate_dict(stacks: list, crate_nrs: list) -> dict:
    crate_dict = {int(i): [] for i in crate_nrs}
    for row in stacks[:-1]:
        n = 0
        for idx, i in enumerate(range(math.ceil(len(row) / 4))):
            if not row[n:n + 4].isspace():
                crate_dict[idx + 1].insert(0, row[n:n + 4].replace(" ", ""))
            n += 4
    return crate_dict


def split_data(data: str):
    stacks, moves = data.split("\n\n")
    return stacks, moves


if __name__ == '__main__':
    data = open('data-day5.txt', 'r').read()
    s, m = split_data(data)
    total_part1 = part1(s, m)
    print(f"total_part1={total_part1}")
    total_part2 = part2(s, m)
    print(f"total_part2={total_part2}")
