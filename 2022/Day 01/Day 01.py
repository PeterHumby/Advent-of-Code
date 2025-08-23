path = __file__[:__file__.rfind(__file__[0])] + __file__[0]
file = open(path + "Input.txt", "r")


elves = sorted([sum([int(n) for n in line.split('\n')]) for line in file.read().split('\n\n')])

print("Part 1: ", elves[-1])
print("Part 2: ", elves[-1] + elves[-2] + elves[-3])