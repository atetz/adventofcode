"""
Day 7: No Space Left On Device
"""
import re


def parse_input(file_name: str) -> str:
    output = ""
    with open(file_name) as in_file:
        for line in in_file:
            output += line
    return output.splitlines()


def main():

    flat_structure = {}
    current_directory = []

    puzzle_input = parse_input("day 7/07-input.txt")
    for line in puzzle_input:
        if line.startswith("$ cd "):
            line = line.replace("$ cd ", "")
            if line == "..":
                current_directory.pop()
                continue
            current_directory.append(line)

        path = "/".join(current_directory)

        if re.match(r"^\d+", line):
            size = int(re.match(r"^\d+", line)[0])
            if flat_structure.get(path):
                flat_structure[path].append(size)
                continue
            flat_structure[path] = [size]

        if path not in flat_structure.keys():
            flat_structure[path] = [0]

    total_folder_sizes = {key: sum(files) for key, files in flat_structure.items()}

    # add size of folder to parent folder
    for folder, size in total_folder_sizes.items():
        for path in total_folder_sizes:
            if path in folder and path != folder:
                total_folder_sizes[path] += size

    small_folders = {
        key: files for key, files in total_folder_sizes.items() if files <= 100000
    }

    filesystem_size = 70000000
    update_size = 30000000
    free_space = filesystem_size - total_folder_sizes["/"]
    space_required_for_update = update_size - free_space

    folders_to_delete = {
        key: files
        for key, files in total_folder_sizes.items()
        if files >= space_required_for_update
    }

    print(f"part 1: {sum(small_folders.values())}")
    print(f"part 2: {min(folders_to_delete.values())}")


if __name__ == "__main__":
    main()
