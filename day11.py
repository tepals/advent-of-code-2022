import re

import numpy as np


def part1(monkey_descrpts: list, n_rounds: int = 20) -> int:
    for i in range(n_rounds):
        for n, monkey in enumerate(monkey_descrpts):
            for old in monkey["start_items"]:
                new = eval(monkey["operation"])  # worry level = old */+- x
                new = int(new / 3)
                if new % monkey["test"] == 0:
                    monkey_descrpts[monkey["if_true"]]["start_items"].append(new)
                else:
                    monkey_descrpts[monkey["if_false"]]["start_items"].append(new)
                monkey_descrpts[n]["insp_items"] += 1
            monkey_descrpts[n]["start_items"] = []

    n_inspections = [m["insp_items"] for m in monkey_descrpts]
    return sorted(n_inspections)[-2] * sorted(n_inspections)[-1]


def part2(monkey_descrpts: list, div_factor: int, n_rounds: int = 10000) -> int:
    for i in range(n_rounds):
        for n, monkey in enumerate(monkey_descrpts):
            old = np.array(monkey["start_items"]).astype(np.uint64) % div_factor
            new = eval(monkey["operation"])
            test_new = new % monkey["test"]
            monkey_descrpts[monkey["if_true"]]["start_items"].extend(list(new[test_new == 0]))
            monkey_descrpts[monkey["if_false"]]["start_items"].extend(list(new[test_new != 0]))
            monkey_descrpts[n]["insp_items"] += len(monkey["start_items"])
            monkey_descrpts[n]["start_items"] = []

    n_inspections = [m["insp_items"] for m in monkey_descrpts]
    return sorted(n_inspections)[-2] * sorted(n_inspections)[-1]


def parse_data(data: str) -> list:
    data = data.split("\n\n")
    pattern = "Monkey (.*):\n.*" \
              "Starting items: (.*)\n.*" \
              "Operation: new = (.*)\n.*" \
              "Test: divisible by (.*)\n.*" \
              "If true: throw to monkey (.*)\n.*" \
              "If false: throw to monkey (.*)"
    monkey_descriptions = []
    div_factor = 1
    for monkey in data:
        description = re.search(pattern, monkey).groups()
        monkey_description = {
            "monkey_n": int(description[0]),
            "start_items": [int(i) for i in description[1].split(",")],
            "operation": description[2],
            "test": int(description[3]),
            "if_true": int(description[4]),
            "if_false": int(description[5]),
            "insp_items": 0
        }
        monkey_descriptions.append(monkey_description)
        div_factor *= int(description[3])
    return monkey_descriptions, div_factor


if __name__ == '__main__':
    data = open('data-day11.txt', 'r').read()
    monkey_descriptions, _ = parse_data(data)
    result_part1 = part1(monkey_descriptions.copy())
    print(f"result_part1={result_part1}")
    data = open('data-day11.txt', 'r').read()
    monkey_descriptions, div_factor = parse_data(data)
    result_part2 = part2(monkey_descriptions, div_factor)
    print(f"result_part2={result_part2}")
