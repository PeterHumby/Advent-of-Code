file = open(r"2021/Inputs/Day 09 Input.txt", "r")

lines = file.read().split('\n')

x, y = len(lines[0]), len(lines)

heights = [int(n) for n in list(''.join(lines))]

def get_neighbours(i): # Get the neighbouring indices around an index i.
    neighbours = [i + x, i - x, i + 1, i - 1]
    if i % x == 0:
        neighbours.pop(-1)
    elif i % x == x - 1:
        neighbours.pop(-2)
    return set([j for j in neighbours if 0 <= j < len(heights)])

def build_basin(i): # Return the size of basin around a point at index i.
    edge, basin = set([i]), set()
    while len(edge) > 0:
        new_edge = set()
        basin |= edge
        for _, j in enumerate(edge):
            new_edge |= set([n for n in get_neighbours(j) if n not in basin and heights[n] != 9])
        edge = new_edge
    return basin

print("Part 1: ", sum([h + 1 for i, h in enumerate(heights) if sum([int(heights[j] <= h) for j in get_neighbours(i)]) == 0]))

basins = []
for i, h in enumerate(heights):
    if h != 9:
        basin = build_basin(i)
        if basin not in basins:
            basins.append(basin)

basin_sizes = sorted([len(b) for b in basins], reverse=True)

print("Part 2: ", basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

