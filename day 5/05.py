"""
Day 5: Supply Stacks
"""


import re
from typing import List
from copy import deepcopy

unarranged_stacks = []
procedures = []

with open("day 5/05-input.txt") as f:
    for line in f:
        if line[0] in ["[", " "]:
            unarranged_stacks.append(line.replace("\n", ""))
        if line[0] == "m":
            procedures.append(re.findall(r"\d+", line))

# Made a mask based on the platform in the input data.
mask = [
    start
    for start, char in enumerate(unarranged_stacks[8], start=1)
    if char.isnumeric()
]


def arrange_stacks(stacks: List) -> List:
    arranged_stacks = []
    for position in mask:
        arranged_stack = [
            stack[position - 1]
            for stack in unarranged_stacks
            if stack[position - 1].isalpha()
        ]
        arranged_stacks.append(arranged_stack)
    return arranged_stacks


# move crates based on procedure
def move_crates(stacks: List, crane_type) -> List:
    for procedure in procedures:
        source = int(procedure[1]) - 1
        destination = int(procedure[2]) - 1
        size = int(procedure[0])
        moving = stacks[source][:size]
        del stacks[source][:size]
        if crane_type == 9000:
            for item in moving:
                stacks[destination].insert(0, item)
        if crane_type == 9001:
            stacks[destination] = moving + stacks[destination]
    return stacks


arranged_stacks = arrange_stacks(unarranged_stacks)

part_one = [char[0] for char in move_crates(deepcopy(arranged_stacks), 9000)]
print(f"The answer to part 1 is: {''.join(part_one)}")

part_two = [char[0] for char in move_crates(deepcopy(arranged_stacks), 9001)]
print(f"The answer to part 2 is: {''.join(part_two)}")
