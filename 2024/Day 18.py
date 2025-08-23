from copy import deepcopy
import time
start_time = time.time()

file = open(r"2024\Inputs/Day 18 Input.txt", "r")

def display(grid, edge=[]):
    display_grid = deepcopy(grid)
    for e in edge:
        display_grid[e[1][1]][e[1][0]] = '@'
    for row in display_grid:
        print(''.join(row))
    print()

w, h = 71, 71

grid = ([['#'] + (['.'] * w) + ['#']]) * h
grid = [(['#'] * (w+2))] + grid + [(['#'] * (w+2))]
last_byte = [0,0]

def add_byte(grid):
    byte = [int(x) for x in file.readline().strip().split(',')]
    grid[byte[1] + 1] = grid[byte[1] + 1][:(byte[0] + 1)] + ['#'] + grid[byte[1] + 1][(byte[0] + 2):]
    return grid, byte

for i in range(1024):
    grid, last_byte = add_byte(grid)



grid[1][1] = 'S'
grid[h][w] = 'E'

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


def gen_maze(x, y, grid): # Generate a graph from a grid starting at x, y.
    maze = {}
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
last_byte = [0,0]

print(min([x[2] for x in ends]))
print("--- Part 1: %s seconds ---" % (time.time() - start_time))
while len(ends) != 0:
    grid, last_byte = add_byte(grid)
    ends = gen_maze(x, y, grid)

print(last_byte)
print("--- Part 2: %s seconds ---" % (time.time() - start_time))