from itertools import product
from functools import cache


path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

num_pad = '789456123#0A'
dir_pad = '#^A<v>'

def optimal(a, b, pad): # Find the optimal path from x -> y on a given pad.
    grid = {tile: (i % 3, i // 3) for i, tile in enumerate(pad)}
    vert = ("^" * (grid[a][1] - grid[b][1])) + ("v" * (grid[b][1] - grid[a][1]))
    hori = ("<" * (grid[a][0] - grid[b][0])) + (">" * (grid[b][0] - grid[a][0]))
    
    if (grid[a][0] == grid['#'][0]) and (grid[b][1] == grid['#'][1]): return {hori + vert + "A"}
    if (grid[b][0] == grid['#'][0]) and (grid[a][1] == grid['#'][1]): return {vert + hori + "A"}

    return {vert + hori + "A", hori + vert + "A"}

# Using a given pad, give the optimal number of moves needed to 
def moves(path, pad): 
        steps = zip("A" + path, path)
        seqs = product(*[optimal(*p,pad) for p in steps])
        return list({"".join(x) for x in seqs})


@cache
def process(code, d):
    if d == 0:
         return len(code)
    return sum( [ min( [process(m, d - 1) for m in moves(block + "A", dir_pad)] ) for block in code[:-1].split('A')])

tot = 0

for line in file:
    line = line.strip()

    tot += int(line[:-1]) * min([process(m, 25) for m in moves(line, num_pad)])

print(tot)