
elves_calories = []
temp_array = []

with open("01-input.txt") as f:
   for line in f:
      if line != '\n':
          line.replace('\n','')
          temp_array.append(int(line))
      if line == '\n':
          elves_calories.append(sum(temp_array))
          temp_array = []

#elf with highest calories
print(max(elves_calories))

#The sum of the first 3 elves
elves_calories.sort(reverse=True)
top_3_total = sum(elves_calories[:3])
print(top_3_total)
