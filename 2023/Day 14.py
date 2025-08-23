import time
start_time = time.time()

file = open(r"Inputs\Day 14 Input.txt", "r")

grid = [list(row) for row in file.read().split('\n')]

def transpose(block): # Transpose a matrix stored as a list of lists.
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]


    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block

def east(grid): # Tilt so all rocks slide east. This is the most convenient to implement and all other directions will be transformed into this.
    for i, row in enumerate(grid):
        prev_block = -1
        for j, c in enumerate(row):
            if c == '#': # If a barrier is reached that isn't the first character.
                round_count = row[(prev_block + 1):j].count('O')
                row = row[:(prev_block + 1)] + list(('.' * (j - prev_block - 1 - round_count)) + ('O' * round_count)) + row[j:]
                prev_block = j

        row = row[:(prev_block + 1)] + list(('.' * ((len(row) - (prev_block + 1)) - row[(prev_block + 1):].count('O'))) + ('O' * row[(prev_block + 1):].count('O')))

        grid[i] = row
    return grid

def north(grid): # Transpose, invert, roll east, invert, transpose = roll north
    grid = transpose(grid)
    grid = [row[::-1] for row in grid]
    grid = east(grid)
    grid = [row[::-1] for row in grid]
    return transpose(grid)

def south(grid):
    grid = transpose(grid)
    grid = east(grid)
    return transpose(grid)

def west(grid):
    grid = [row[::-1] for row in grid]
    grid = east(grid)
    return [row[::-1] for row in grid]

def get_load(grid):
    grid = transpose(grid)
    grid = [row[::-1] for row in grid]

    total = 0

    for _, row in enumerate(grid):
        for i, c in enumerate(row):
            if c == 'O':
                total += (i + 1)

    return total

# Part 1
print(get_load(north(grid)))

loads = []

# Part 2 - let the process run until a loop is recognised, then figure out which part of the loop the 1000000000th cycle ends on. (Last bit is manual)
for i in range(1000000000):
    grid = north(grid)
    grid = west(grid)
    grid = south(grid)
    grid = east(grid)
    load = get_load(grid)
    if load in loads:
        print("MATCH", loads.index(load))
    loads.append(load)

    input((i, load))

print(loads)


