from copy import deepcopy


path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

grid = [list(row.strip()) for row in file]

start_index = ''.join([''.join(row) for row in grid]).index('S')
end_index = ''.join([''.join(row) for row in grid]).index('E')


x, y = start_index % len(grid[0]), start_index // len(grid)
end_x, end_y = end_index % len(grid[0]), end_index // len(grid)

def display(grid, edge=[]):
    display_grid = deepcopy(grid)
    for e in edge:
        display_grid[e[1][1]][e[1][0]] = '@'
    for row in display_grid:
        print(''.join(row))
    print()

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
        '''
        display(grid, edge)
        print(len(edge))
        
        for p in edge:
            print(p[1], p[0][-1], p[2])
        input()
        '''
        for path in edge:
            if path[1] != (end_x, end_y):
                e_x, e_y = path[1][0], path[1][1]
                p_x, p_y = path[0][-1][0], path[0][-1][1]

                checks = [(e_x - 1, e_y), (e_x + 1, e_y), (e_x, e_y - 1), (e_x, e_y + 1)]

                for check in checks:
                    if (check != (p_x, p_y)) and (grid[check[1]][check[0]] != '#'):
                        if check == (e_x + (e_x - p_x), e_y + (e_y - p_y)):
                            if check not in maze or ((check in maze) and (path[2] + 1 <= maze[check])):
                                new_edge.append((path[0] + [path[1]], check, path[2] + 1))
                                maze[check] = path[2] + 1


                        else:
                            if check not in maze or ((check in maze) and (path[2] + 1001 <= maze[check])):
                                new_edge.append((path[0] + [path[1]], check, path[2] + 1001))
                                maze[check] = path[2] + 1001

            else:
                ends.append(path)

        edge = new_edge

    return ends

tot = 0
ends = gen_maze(x, y, grid)
score = min([x[2] for x in ends])
print(ends)
path_tiles = []

for path in ends:
    if path[2] == score:
        path_tiles += path[0]
display_optimal(grid, path_tiles)
print(len(list(set(path_tiles))))