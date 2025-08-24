from copy import deepcopy

file = open(r"2024/Inputs/Day 15 Input.txt", "r")

data = file.read().split('\n\n')

grid = [list(row) for row in data[0].split('\n')]
moves = [m for i, m in enumerate(data[1]) if m != '\n']

box_id = 0
box_positions = {} # id system for boxes containing halves

def display(grid):
    for row in grid:
        row = list(map(lambda x: x[0], row))
        print(''.join(row))
    print()

x, y = 0, 0
for j in range(len(grid)):
    row = grid[j]
    for i in range(len(grid) - 1, -1, -1):
            if row[i] == '@':
                x = 2*i
                y = j


            if row[i] == 'O':
                box_positions[box_id] = [[[i,j], [i+1, j]]]
                row[i] = ']' + str(box_id)
                row.insert(i, '[' + str(box_id))
                box_id += 1
            
            else:
                row.insert(i, row[i])

grid[y][x + 1] = '.'

def get_adj(x, y, dir):
    if dir == '^':
        return x, y-1
    elif dir == '>':
        return x+1, y
    elif dir == 'v':
        return x, y+1
    elif dir == '<':
        return x-1,y
    else:
        return x,y

def push_line(x, y, dir, grid): # Push all elements on and after (x,y) in the direction given.
        adj_x, adj_y = get_adj(x, y, dir)

        if grid[adj_y][adj_x] == '.':
            grid[adj_y][adj_x] = grid[y][x]
            grid[y][x] = '.'
            return grid
        elif grid[adj_y][adj_x] == '#':
            return grid
        else:
            grid = push_line(adj_x, adj_y, dir, grid)
            if grid[adj_y][adj_x] == '.':
                grid[adj_y][adj_x] = grid[y][x]
                grid[y][x] = '.'
        return grid

def push_block(x, y, dir, grid):
    if grid[y][x][0] == '[':
        b_x, b_y = x + 1, y
    elif grid[y][x][0] == ']':
        b_x, b_y = x - 1, y
    
    adj_x, adj_y = get_adj(x, y, dir)
    b_adj_x, b_adj_y = get_adj(b_x, b_y, dir)

    if (grid[adj_y][adj_x] == '.') and (grid[b_adj_y][b_adj_x] == '.'):
        grid[adj_y][adj_x] = grid[y][x]
        grid[b_adj_y][b_adj_x] = grid[b_y][b_x]
        grid[y][x] = '.'
        grid[b_y][b_x] = '.'
        return grid
    
    if (grid[adj_y][adj_x] == '#') or (grid[b_adj_y][b_adj_x] == '#'):
        return grid
    
    original_grid = deepcopy(grid)
    
    if (grid[adj_y][adj_x] != '.'):
        grid = push_block(adj_x, adj_y, dir, grid)
        
    if (grid[b_adj_y][b_adj_x] != '.'):
        grid = push_block(b_adj_x, b_adj_y, dir, grid)
        
    if (grid[adj_y][adj_x] == '.') and (grid[b_adj_y][b_adj_x] == '.'):
        grid[adj_y][adj_x] = grid[y][x]
        grid[b_adj_y][b_adj_x] = grid[b_y][b_x]
        grid[y][x] = '.'
        grid[b_y][b_x] = '.'
        return grid
    else:
        return original_grid



def push(x, y, dir, grid): # Push a box containing the coords (x,y) in the direction given.
    if grid[y][x][0] in ['.', '#']:
        return grid

    adj_x, adj_y = get_adj(x, y, dir)
    if dir in ['<', '>']:
        return push_line(x, y, dir, grid)
    elif dir in ['^', 'v']:
        grid = push_block(x, y, dir, grid)
        return grid
    
        


def move(x, y, dir, grid):
    adj_x, adj_y = get_adj(x, y, dir)
    original_grid = deepcopy(grid)
    if grid[adj_y][adj_x] == '#':
        return x, y, grid
    
    elif grid[adj_y][adj_x] == '.':
        grid[adj_y][adj_x] = grid[y][x]
        grid[y][x] = '.'
        return adj_x, adj_y, grid

    else:
        grid = push(adj_x, adj_y, dir, grid)
        if grid[adj_y][adj_x] == '.':
            grid[adj_y][adj_x] = grid[y][x]
            grid[y][x] = '.'
            return adj_x, adj_y, grid
        else:
            return x, y, original_grid
    return x, y, original_grid

display(grid)


for m in moves:
    x, y, grid = move(x, y, m, grid)

display(grid)

box_scores = {}
tot = 0
for j in range(len(grid)):
    row = grid[j]
    for i in range(len(grid[0])):
        if grid[j][i][0] in ['[', ']']:
            if grid[j][i][1:] not in box_scores:
                box_scores[grid[j][i][1:]] = (100 * j) + i

for k in box_scores:
    tot += box_scores[k]

print(tot)
        
        
