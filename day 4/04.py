"""
    Day 4: Camp Cleanup
"""


def get_section_range(section):
    start = int(section.split("-")[0])
    stop = int(section.split("-")[1])
    return {start} if start == stop else set(range(start, stop + 1))


overlapping_pairs = 0
overlapping_assignments = 0
with open("day 4/04-input.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        pair = line.split(",")
        section_1 = get_section_range(pair[0])
        section_2 = get_section_range(pair[1])
        if section_1.issubset(section_2) or section_2.issubset(section_1):
            overlapping_pairs += 1
        for assignment in section_1:
            if assignment in section_2:
                overlapping_assignments += 1
                break

print(f"{overlapping_pairs} assignments fully contain the other.")
print(f"{overlapping_assignments} assignments overlap with the other.")
