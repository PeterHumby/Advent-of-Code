file = open(r"2022\Inputs\Day 01 Input.txt", "r")


elves = sorted([sum([int(n) for n in line.split('\n')]) for line in file.read().split('\n\n')])

print("Part 1: ", elves[-1])
print("Part 2: ", elves[-1] + elves[-2] + elves[-3])