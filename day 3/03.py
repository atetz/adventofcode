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

def get_itemtype_priority(rucksack: str) -> int:
    divided_rucksack = divide_rucksack(rucksack)
    item_in_both_compartments = get_item_in_both_compartments(divided_rucksack)
    return priority.index(item_in_both_compartments)+ 1


priority = ascii_lowercase + ascii_uppercase

def main():  # sourcery skip: comprehension-to-generator
    rucksacks = []
    with open("day 3/03-input.tx") as f:
        for line in f:
            line = line.replace('\n','')
            rucksacks.append(line)
            
    sum_of_itempriorities = sum([get_itemtype_priority(rucksack) for rucksack in rucksacks])
    print(f"The sum of the priorities of the item types is: {sum_of_itempriorities}")

if __name__ == "__main__":
    main()