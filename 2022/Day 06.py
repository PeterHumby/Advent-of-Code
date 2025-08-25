file = open(r"2022/Inputs/Day 06 Input.txt", "r")

data = file.read().split('\n')


p1_tot, p2_tot = 0, 0

for _, buffer in enumerate(data):
    i, j = 4, 14
    
    while len(set(buffer[(i-4):i])) != 4:
        i += 1
    
    while len(set(buffer[(j-14):j])) != 14:
        j += 1

    p1_tot += i
    p2_tot += j

print("Part 1: ", p1_tot)
print("Part 2: ", p2_tot)
