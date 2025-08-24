from copy import deepcopy
import time
start_time = time.time()

file = open(r"2024/Inputs/Day 20 Input.txt", "r")

def display(grid, edge=[]):
    display_grid = deepcopy(grid)
    for e in edge:
        display_grid[e[1][1]][e[1][0]] = '@'
    for row in display_grid:
        print(''.join(row))
    print()

grid = [list(row.strip()) for row in file]

start_index = ''.join([''.join(row) for row in grid]).index('S')
end_index = ''.join([''.join(row) for row in grid]).index('E')


x, y = start_index % len(grid[0]), start_index // len(grid)
end_x, end_y = end_index % len(grid[0]), end_index // len(grid)


def display_optimal(grid, optimal_tiles):
    display_grid = deepcopy(grid)
    for tile in optimal_tiles:
        if grid[tile[1]][tile[0]] != '#':
            display_grid[tile[1]][tile[0]] = 'O'
    for row in display_grid:
        print(''.join(row))
    print()


def gen_maze(x, y, grid, prev_x=None, prev_y=None):
    maze = {}
    if (prev_x != None) and (prev_y != None):

        edge = [([(prev_x, prev_y)], (x,y), 0)] # Previous edge, edge, and cost to get to that edge.
    else:
        edge = [([(x-1, y)], (x,y), 0)] # Previous edge, edge, and cost to get to that edge.
    ends = []
    while len(edge) > 0:
        new_edge = []
        edge = sorted(edge, key=lambda x: x[2], reverse=True)
        for path in edge:
            if path[1] != (end_x, end_y):
                e_x, e_y = path[1][0], path[1][1]
                p_x, p_y = path[0][-1][0], path[0][-1][1]

                checks = [(e_x - 1, e_y), (e_x + 1, e_y), (e_x, e_y - 1), (e_x, e_y + 1)]

                for check in checks:
                    if (check != (p_x, p_y)) and (grid[check[1]][check[0]] != '#'):
                        if check not in maze or ((check in maze) and (path[2] + 1 < maze[check])):
                            new_edge.append((path[0] + [path[1]], check, path[2] + 1))
                            maze[check] = path[2] + 1

            else:
                ends.append(path)

        edge = new_edge

    return ends

ends = gen_maze(x, y, grid)
tot = 0

# Part 1
lim = 100
for end in ends:
    path = end[0][1:] + [(end_x, end_y)]
    for i in range(len(path) - lim):
        for j in range(i + lim, len(path)):
            dist = abs(path[j][1] - path[i][1]) + abs(path[j][0] - path[i][0])
            if  (dist == 2) and (j - i - dist >= lim):
                tot += 1

print(tot)

print("--- Part 1: %s seconds ---" % (time.time() - start_time))

# Part 2
tot = 0
lim = 100
for end in ends:
    path = end[0][1:] + [(end_x, end_y)]
    for i in range(len(path) - lim):
        for j in range(i + lim, len(path)):
            dist = abs(path[j][1] - path[i][1]) + abs(path[j][0] - path[i][0])
            if  (dist <= 20) and (j - i - dist >= lim):
                tot += 1

print(tot)

print("--- Part 2: %s seconds ---" % (time.time() - start_time))
