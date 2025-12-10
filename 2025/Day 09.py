from itertools import combinations, pairwise

file = open(r"2025/Inputs/Day 09 Input.txt", "r")

tiles = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in file.read().split('\n')]
green = [((min(a, c), min(b, d)), (max(a, c), max(b, d))) for (a, b), (c, d) in pairwise(tiles + [tiles[0]])]

p1_max, p2_max = 0, 0
for (x,y), (u,v) in [((min(a, c), min(b, d)), (max(a, c), max(b, d))) for (a, b), (c, d) in combinations(tiles, 2)]:
    size = (u - x + 1) * (v - y + 1)

    p1_max = max(p1_max, size)

    if size > p2_max:
        for (p, q), (r, s) in green:
            if p < u and q < v and r > x and s > y: 
                break

        else: p2_max = size

print("Part 1: ", p1_max)

print("Part 2: ", p2_max)