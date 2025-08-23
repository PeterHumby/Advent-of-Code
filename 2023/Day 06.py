import re
from math import ceil, floor

file = open(r"2023\Inputs\Day 06 Input.txt", "r")

data = file.read().split('\n')

tot = 1

# # Part 1
# times = [int(n.group()) for n in re.finditer(r'\d+', data[0])]
# distances = [int(n.group()) for n in re.finditer(r'\d+', data[1])]


# Part 2
times = [int(''.join([n.group() for n in re.finditer(r'\d+', data[0])]))]
distances = [int(''.join([n.group() for n in re.finditer(r'\d+', data[1])]))]

for i, time in enumerate(times):
    distance = distances[i]

    det = ((time**2) - (4 * distance)) ** 0.5
    lower = floor( ((time - det) / 2) + 1)
    upper = ceil( ((time + det) / 2) - 1)

    tot *= (upper - lower + 1)

print(tot)

