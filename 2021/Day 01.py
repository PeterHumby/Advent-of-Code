file = open(r"2021/Inputs/Day 01 Input.txt", "r")

depths = [int(n) for n in file.read().split('\n')]

# Part 1
p1_output = 0

for n, d in enumerate(depths[1:]):
    p1_output += int(d > depths[n])

print("Part 1: ", p1_output)


# Part 2
p2_output = 0

for n, _ in enumerate(depths[1:-1]):
    p2_output += int(sum(depths[n+1:n+4]) > sum(depths[n:n+3]))

print("Part 2: ", p2_output)