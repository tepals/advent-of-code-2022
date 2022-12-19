import numpy as np
from pprint import pprint


def part1(data: str) -> int:
    cycle = 0
    register_x = 1
    signal_strength = 0
    for cmd, value, n_cycles in data:
        for i in range(n_cycles):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strength += cycle * register_x
        register_x += value
    return signal_strength


def part2(data: str) -> list:
    cycle = 0
    sprite_position = np.array([0, 1, 2])
    current_crt = ""
    crt_rows = []
    for cmd, value, n_cycles in data:
        for i in range(n_cycles):
            if cycle in sprite_position:
                current_crt += "#"
            else:
                current_crt += "."
            cycle += 1
            if len(current_crt) == 40:
                crt_rows.append(current_crt)
                current_crt = ""
                cycle = 0
        sprite_position += value
    return crt_rows


def parse_data(data: str) -> list:
    program = []
    for row in data.split("\n"):
        if row.startswith("noop"):
            # ------------- cmd, value, n_cycles
            program.append((row, 0, 1))
        elif row.startswith("addx"):
            cmd, v = row.split(" ")
            # ------------- cmd, value, n_cycles
            program.append((cmd, int(v), 2))
    return program


if __name__ == '__main__':
    data = open('data-day10.txt', 'r').read()
    data = parse_data(data)
    print(data)
    result_part1 = part1(data)
    print(f"result_part1={result_part1}")
    result_part2 = part2(data)
    print("result_part2:")
    pprint(result_part2)
