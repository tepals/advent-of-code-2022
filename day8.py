import numpy as np


def part1(data: np.array) -> int:
    visible_trees_left = get_visible_trees(data)
    visible_trees_right = np.fliplr(get_visible_trees(np.fliplr(data)))
    visible_trees_top = get_visible_trees(data.T).T
    visible_trees_bottom = np.fliplr(get_visible_trees(np.fliplr(data.T))).T
    vis_trees = visible_trees_left + visible_trees_right + visible_trees_top + visible_trees_bottom
    v = np.ones_like(vis_trees)
    v[1:-1, 1:-1] = vis_trees[1:-1, 1:-1]
    v[v > 0] = 1
    return np.sum(v)


def part2(data: np.array) -> int:
    visibility_left = get_tree_visibility(data)
    visibility_right = np.fliplr(get_tree_visibility(np.fliplr(data)))
    visibility_top = get_tree_visibility(data.T).T
    visibility_bottom = np.fliplr(get_tree_visibility(np.fliplr(data.T))).T
    v = np.multiply(np.multiply(np.multiply(
        visibility_left, visibility_right),
        visibility_top),
        visibility_bottom)
    return np.max(v)


def get_tree_visibility(data: np.array) -> np.array:
    visibility = np.zeros_like(data)
    for idx1, row in enumerate(data):
        vis_cnt = np.zeros_like(row)
        for idx2, i in enumerate(row):
            cnt = 0
            for j in range(1, len(row) - idx2):
                if row[idx2 + j] < row[idx2]:
                    cnt += 1
                else:
                    cnt += 1  # you always see 1 tree except on the borders
                    break
            vis_cnt[idx2] = cnt
        visibility[idx1, :] = vis_cnt
    return visibility


def get_visible_trees(data: np.array) -> np.array:
    visible_trees = np.zeros_like(data)
    for idx, row in enumerate(data):
        visible_trees[idx, :] = get_row_visibility(row.copy())
    return visible_trees


def get_row_visibility(row: np.array) -> np.array:
    max_row = row[0]
    for idx, i in enumerate(row):
        if i > max_row:
            max_row = i
            row[idx] = True
        else:
            row[idx] = False
    return row


def to_int_array(data: str) -> np.array:
    trees = []
    for row in data.split("\n"):
        trees.append(list(row))
    return np.array(trees).astype(int)


if __name__ == '__main__':
    data = open('data-day8.txt', 'r').read()
    data = to_int_array(data)
    result_part1 = part1(data)
    print(f"result_part1={result_part1}")
    result_part2 = part2(data)
    print(f"result_part2={result_part2}")
