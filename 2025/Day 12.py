from functools import cache

file = open(r"2025/Inputs/Day 12 Input.txt", "r")

data = file.read().split('\n\n')

sizes = [p.count('#') for p in data[:-1]]

fit_count = 0
for i, req in enumerate([[list(map(int, l.split(': ')[0].split('x'))), list(map(int, l.split(': ')[1].split(' ')))] for l in data[-1].split('\n')]):
    x,y = req[0]
    presents = req[1]

    if sum(presents) <= (x // 3) * (y // 3):
        fit_count += 1
    elif sum([s * presents[i] for i, s in enumerate(sizes)]) <= x * y:
        input(f"Check requirement {i}")

print("Part 1: ", fit_count)

    

