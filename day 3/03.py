from typing import List
from string import ascii_lowercase, ascii_uppercase
""" part one:
Find the item type that appears in both compartments of each rucksack. 
What is the sum of the priorities of those item types?
"""

def divide_rucksack(rucksack: str) -> List:
    items_per_compartment = len(rucksack) //2
    return [rucksack[:items_per_compartment], rucksack[-items_per_compartment:]]

def get_item_in_both_compartments(rucksack_compartments: List) -> str:
    for char in rucksack_compartments[0]:
        if char in rucksack_compartments[1]:
            return char

def get_itemtype_priority(item: str) -> int:
    return priority.index(item)+ 1


def chunker(seq, chunksize) -> List:
    """Generator function that chunks a large list into smaller lists."""
    res = []
    for i in seq:
        res.append(i)
        if len(res) == chunksize:
            yield res
            res = []
    if res:
        yield res

def get_group_badge_type(group: List, size: int) -> str:
    unique_items_in_rucksack = ["".join(set(rucksack)) for rucksack in group]
    all_items = "".join(unique_items_in_rucksack)
    for char in all_items:
        if all_items.count(char) >= size:
            return char

priority = ascii_lowercase + ascii_uppercase

def main():  # sourcery skip: comprehension-to-generator
    rucksacks = []
    with open("day 3/03-input.tx") as f:
        for line in f:
            line = line.replace('\n','')
            rucksacks.append(line)
    
    rucksack_priorities = []
    for rucksack in rucksacks:
        divided_rucksack = divide_rucksack(rucksack)
        item_in_both_compartments = get_item_in_both_compartments(divided_rucksack)
        rucksack_priorities.append(get_itemtype_priority(item_in_both_compartments))

    print(f"The sum of the priorities of the item types is: {sum(rucksack_priorities)}")

    all_groups_of_elves = chunker(rucksacks,3)
    group_badge_priorites = []

    for group in all_groups_of_elves:
        badge_type = get_group_badge_type(group,3)
        group_badge_priorites.append(get_itemtype_priority(badge_type))
    print(f"The sum of the priorities of the group is: {sum(group_badge_priorites)}")


if __name__ == "__main__":
    main()