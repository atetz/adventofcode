"""
    part one: find overlapping sections
"""


def get_section_range(section):
    start = int(section.split("-")[0])
    stop = int(section.split("-")[1])
    return {start} if start == stop else set(range(start, stop + 1))


pairs = 0
with open("day 4/04-input.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        pair = line.split(",")
        section_1 = get_section_range(pair[0])
        section_2 = get_section_range(pair[1])
        if section_1.issubset(section_2) or section_2.issubset(section_1):
            print(True)
            pairs += 1
print(pairs)
