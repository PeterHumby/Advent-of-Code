from itertools import pairwise

def transpose(block):
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]

    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block

file = open(r"Inputs\Day 11 Input.txt", "r")

data = file.read().split('\n')

empty_rows, empty_cols = [], []

for i, row in enumerate(data):
        if set(row) == set(['.']):
            empty_rows.append(i)

for i, col in enumerate(transpose(data)):
        if set(col) == set(['.']):
            empty_cols.append(i)

line_length = len(data[0])

data = ''.join([''.join(row) for row in data])

galaxy_indices = [i for i, c in enumerate(data) if c == '#']

tot = 0

for i, g1 in enumerate(galaxy_indices):
    for j, g2 in enumerate(galaxy_indices[(i + 1):]):
        g1_x, g1_y = g1 % line_length, g1 // line_length
        g2_x, g2_y = g2 % line_length, g2 // line_length

        context_empty_rows = len(list(filter(lambda y: (min([g1_y, g2_y])) < y and (max([g1_y, g2_y]) > y), empty_rows)))
        context_empty_cols = len(list(filter(lambda x: (min([g1_x, g2_x])) < x and (max([g1_x, g2_x]) > x), empty_cols)))

        # Part 1
        # tot += (abs(g1_x - g2_x) + abs(g1_y - g2_y)) + context_empty_rows + context_empty_cols

        # Part 2
        tot += (abs(g1_x - g2_x) + abs(g1_y - g2_y)) + (999999*(context_empty_rows + context_empty_cols))

print(tot)

