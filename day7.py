class Directories:

    def __init__(self, parent):
        self.structure = {parent: {'filesize': 0}}
        self.current_dir = parent
        self.parents = []

    def add_directory(self, name):
        self.parents.append(name)
        nested_set(self.structure, self.parents, {'filesize': 0})

    def add_file(self, filesize, name):
        temp_list = self.parents.copy()
        for i in range(len(temp_list)):
            temp_list.append("filesize")
            nested_set_add(self.structure, temp_list, filesize)
            temp_list.pop()
            temp_list.pop()

        temp_list = self.parents.copy()
        temp_list.append(name)
        nested_set(self.structure, temp_list, filesize)


def nested_set(dic, keys, value):
    """https://stackoverflow.com/a/13688108"""
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


def nested_set_add(dic, keys, value):
    """https://stackoverflow.com/a/13688108"""
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] += value


def create_dirs_structure(statements):
    dirs = Directories("/")
    for line in statements.split("\n"):
        if line.startswith("$ cd"):
            _, dirname = line.split("cd ")
            if dirname != "..":
                dirs.add_directory(dirname)
            else:
                dirs.parents.pop()
        elif line.startswith("$"):
            continue
        else:
            if not line.startswith("dir"):
                fsize, n = line.split(" ")
                dirs.add_file(int(fsize), n)
    return dirs


def recursive_items(dictionary):
    """https://stackoverflow.com/a/39234154"""
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)


def part1(data):
    dirs = create_dirs_structure(data)

    sum_of_total_sizes = 0
    for key, value in recursive_items(dirs.structure):
        if key == "filesize" and value <= 100000:
            sum_of_total_sizes += value

    return sum_of_total_sizes


def part2(data, total_space=70000000, needed_space=30000000):
    dirs = create_dirs_structure(data)
    available_space = total_space - dirs.structure["/"]["filesize"]
    if available_space >= needed_space:
        return 0  # no need to delete a dir, so size is 0
    required_space = needed_space - available_space

    large_sizes = []
    for key, value in recursive_items(dirs.structure):
        if key == "filesize" and value >= required_space:
            large_sizes.append(value)

    return min(large_sizes)


if __name__ == '__main__':
    data = open('data-day7.txt', 'r').read()
    # print(data)
    print("")
    result_part1 = part1(data)
    print(f"result_part1={result_part1}")
    result_part2 = part2(data)
    print(f"result_part2={result_part2}")
