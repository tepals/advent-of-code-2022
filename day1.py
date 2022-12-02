def part_1(data_groups):
    max_calories = 0
    for group in data_groups:
        calories = sum(int(i) for i in group.split("\n"))
        if calories > max_calories:
            max_calories = calories
    return max_calories


def part_2(data_groups):
    calories_pp = []
    for group in data_groups:
        calories = sum(int(i) for i in group.split("\n"))
        calories_pp.append(calories)

    return sum(sorted(calories_pp)[::-1][:3])


if __name__ == '__main__':
    data = open('data-day1.txt', 'r').read()
    groups = data.split("\n\n")
    max_cal = part_1(groups)
    top_3 = part_2(groups)
    print(f"max calories: {max_cal}")
    print(f"top 3 max calories: {top_3}")
