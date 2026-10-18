from functools import cache

file = open(r"2021/Inputs/Day 07 Input.txt", "r")
crabs = [int(c) for c in file.read().split(',')]

p1_fuel_costs = [sum([abs(x - c) for c in crabs]) for x in range(0, max(crabs) + 1)]
p2_fuel_costs = [sum([abs(x - c) * (abs(x - c) + 1) / 2 for c in crabs]) for x in range(0, max(crabs) + 1)]

print("Part 1: ", min(p1_fuel_costs))
print("Part 2: ", min(p2_fuel_costs))