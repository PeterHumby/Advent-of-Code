file = open(r"2025/Inputs/Day 01 Input.txt", "r")

dial = 50
p1_count = 0
p2_count = 0

for t in file.read().split('\n'):
    prev_dial = dial
    dx = int(t[1:])
    p2_count += (dx // 100)
    dx %= 100

    dial += int({'L': -1, 'R': 1}[t[0]]) * dx
    
    if dial not in range(1, 100):
        p1_count += int(dial == 0 or dial == 100)
        p2_count += 1 - int(prev_dial == 0)

    dial %= 100
    
print("Part 1: ", p1_count)
print("Part 2: ", p2_count)
