import numpy as np

move_direction = {
    'R': {"x": 1, "y": 0},
    'L': {"x": -1, "y": 0},
    'U': {"y": 1, "x": 0},
    'D': {"y": -1, "x": 0},
}


def part1(moves: list) -> int:
    x = 0
    y = 0
    pos_tail = [(0, 0)]
    tail_x = 0
    tail_y = 0

    for d, m in moves:
        for i in range(m):
            x += move_direction[d]["x"]
            y += move_direction[d]["y"]

            if np.sqrt((tail_x - x) ** 2 + (tail_y - y) ** 2) > np.sqrt(2):
                tail_x, tail_y = get_position_tail(x, y, tail_x, tail_y)
                pos_tail.append((tail_x, tail_y))

    pos_tail = np.array(pos_tail)
    pos_tail = pos_tail - np.min(pos_tail)

    visited_tails = np.zeros((np.max(pos_tail[:, 0] + 1),
                              np.max(pos_tail[:, 1] + 1)))
    visited_tails[pos_tail[:, 0], pos_tail[:, 1]] = 1
    output_tails = np.flipud(visited_tails.T)  # only needed for visualization
    return np.sum(output_tails).astype(int)


def part2(moves: list) -> int:
    pos_head = (0, 0)
    pos_tail = [(0, 0)]
    tail_x = [0, ] * 9
    tail_y = [0, ] * 9

    for d, m in moves:
        for i in range(m):
            x = pos_head[0] + move_direction[d]["x"]
            y = pos_head[1] + move_direction[d]["y"]
            pos_head = (x, y)
            for idx, t in enumerate(zip(tail_x, tail_y)):
                if np.sqrt((t[0] - x) ** 2 + (t[1] - y) ** 2) > np.sqrt(2):
                    x, y = get_position_tail(x, y, t[0], t[1])
                    tail_x[idx] = x
                    tail_y[idx] = y
                else:
                    x, y = t
            pos_tail.append((tail_x[-1], tail_y[-1]))
    pos_tail = np.array(pos_tail)
    pos_tail = pos_tail - np.min(pos_tail)

    visited_tails = np.zeros((np.max(pos_tail[:, 0] + 1),
                              np.max(pos_tail[:, 1] + 1)))
    visited_tails[pos_tail[:, 0], pos_tail[:, 1]] = 1
    output_tails = np.flipud(visited_tails.T)  # only needed for visualization
    return np.sum(output_tails).astype(int)


def get_position_tail(new_pos_head_x: int, new_pos_head_y: int, last_pos_tail_x: int, last_pos_tail_y: int) -> tuple:
    new_pos_tail_x = last_pos_tail_x + np.sign(new_pos_head_x - last_pos_tail_x)
    new_pos_tail_y = last_pos_tail_y + np.sign(new_pos_head_y - last_pos_tail_y)
    return new_pos_tail_x, new_pos_tail_y


def parse_data(data: str) -> list:
    moves = []
    for row in data.split("\n"):
        direction, steps = row.split(" ")
        moves.append((direction, int(steps)))
    return moves


if __name__ == '__main__':
    data = open('data-day9.txt', 'r').read()
    moves = parse_data(data)
    result_part1 = part1(moves)
    print(f"result_part1={result_part1}")
    result_part2 = part2(moves)
    print(f"result_part2={result_part2}")
