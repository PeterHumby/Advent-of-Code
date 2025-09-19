file = open(r"2022/Inputs/Day 14 Input.txt", "r")
paths = [[tuple([int(n) for n in x.split(',')]) for x in line.split(' -> ')] for line in file.read().split('\n')]

rocks = {}

def sign(a, b):
    if a == b:
        return 0
    return int((a - b) // ((a - b)**2)**0.5)

def fall(x, y, floor): # Get the coordinate of the position that a grain of sand will stop at when falling vertically, or None if unblocked.
    if len(rocks.get(x, [])) > 0:
        below = set(filter(lambda h: h > y, rocks[x]))
        if len(below) > 0:
            return x, min(below) - 1
    return x, floor

def drop(r, floor):
    x, y = 500, 0

    while True:
        if y + 1 in r.get(x, []):
            if y + 1 not in r.get(x - 1, []):
                x -= 1
                y += 1
            elif y + 1 not in r.get(x + 1, []):
                x += 1
                y += 1
            else:
                return x, y
        else:
            x, y = fall(x, y, floor)
            if y == floor:
                return x, y
for p in paths:
    for x1, x2 in zip(p, p[1:]):
        dx, dy = sign(x2[0], x1[0]), sign(x2[1], x1[1])
        for i in range(abs(x2[0] - x1[0]) + abs(x2[1] - x1[1]) + 1):
            rocks[x1[0] + i*dx] = rocks.get(x1[0] + i*dx, set()).union(set([x1[1] + i*dy]))
    
def simulate(r, part=1):

    floor = None
    if part == 2:
        floor = max([max(c) for c in r.values()]) + 1

    x, y = drop(r, floor)
    count = 0
    
    while (y != None) and ((x, y) != (500, 0)):
        r[x] = r.get(x, set()).union(set([y]))
        x, y = drop(r, floor)
        count += 1
    
    return count + (part - 1) # Adjust with part - 1 for the final grain of sand needed in part 2.

print(simulate(rocks, part=2))


