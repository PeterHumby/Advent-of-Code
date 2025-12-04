file = open(r"2025/Inputs/Day 04 Input.txt", "r")

rolls = {x + y*1j for y, row in enumerate(file.read().split('\n')) for x, obj in enumerate(row) if obj == '@'}

acc = 0
initial_loop = True
while True:
    removable = set()

    for r in rolls:
        adjs = {r - 1, r + 1, r - 1 - 1j, r - 1 + 1j, r - 1j, r + 1j, r + 1 - 1j, r + 1 + 1j}
        if len(adjs.intersection(rolls)) < 4:
            removable.add(r)
            acc += 1
    
    if initial_loop:
        print("Part 1: ", acc)
        initial_loop = False

    if len(removable) == 0:
        break
    else:
        rolls -= removable



print("Part 2: ", acc)