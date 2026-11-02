file = open(r"2021/Inputs/Day 11 Input.txt", "r")

lines = file.read().split('\n')

w, h = len(lines[0]), len(lines)

neighbours = {}
levels = {}
for i, e in enumerate(''.join(lines)): # Find the neighbouring indices in the grid for each index
    adj = set([i + 1, i - 1, i + w, i - w, i + w - 1, i + w + 1, i - w - 1, i - w + 1])
    if i % w == 0:
        adj -= set([i - 1, i - w - 1, i + w - 1])
    elif i % w == w - 1:
        adj -= set([i + 1, i + w + 1, i - w + 1])
    if i // w == 0:
        adj -= set([i - w - 1, i - w, i - w + 1])
    elif i // w == h - 1:
        adj -= set([i + w - 1, i + w, i + w + 1])
    neighbours[i] = adj
    levels[i] = int(e)


def step(levels):
    flashed = []
    levels = {i: e + 1 for i, e in levels.items()}
    flash_queue = [i for i, e in levels.items() if e > 9]

    while len(flash_queue) > 0:
        j = flash_queue.pop(0)
        flashed.append(j)
        adj = neighbours[j]
        for k in adj:
            levels[k] += 1
        flash_queue += [k for k in adj if levels[k] > 9 and k not in flashed]
        flash_queue = [k for k in flash_queue if k not in flashed]
    return len(flashed), {i: 0 if i in flashed else e for i, e in levels.items()}


def display(levels):
    for i, e in levels.items():
        print(e, end= '' if i % w != w - 1 else '\n')
    input()

total_flashes = 0

i = 0
while True:
    flashes, levels = step(levels)
    # display(levels)
    if i < 100:
        total_flashes += flashes
    elif flashes == len(levels):
        input(f"Part 2: {i + 1}")

    if i == 99:
        print("Part 1: ", total_flashes)

    i += 1




