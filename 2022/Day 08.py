file = open(r"2022/Inputs/Day 08 Input.txt", "r")

grid = [[int(n) for n in list(line)] for line in file.read().split('\n')]

def transpose(block): # Transpose a matrix stored as a list of lists.
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]


    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block

def get_left_visible(grid): # Get the coords of trees visible from the left.
    visible = set()

    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            if [p_h for p_h in row[:j] if p_h >= h] == []:
                visible.add((j, i))
    
    return visible

def get_right_visible(grid): # Get the coords of trees visible from the right.
    grid = [row[::-1] for row in grid]
    visible = set()

    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            if [p_h for p_h in row[:j] if p_h >= h] == []:
                visible.add((len(row) - j - 1, i))
    
    return visible

def get_top_visible(grid): # Get the coords of trees visible from the top.
    grid = transpose(grid)
    visible = set()

    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            if [p_h for p_h in row[:j] if p_h >= h] == []:
                visible.add((i, j))

    return visible

def get_bottom_visible(grid): # Get the coords of trees visible from the bottom.
    grid = [row[::-1] for row in transpose(grid)]
    visible = set()

    for i, row in enumerate(grid):
        for j, h in enumerate(row):
            if [p_h for p_h in row[:j] if p_h >= h] == []:
                visible.add((i, len(row) - j - 1))

    return visible

def get_scenic_score(x, y, grid): # Get the number of trees visible from the tree at (x, y).
    check_height = grid[y][x]
    

    # Trees visible to the left
    left_visible = len(grid[y][:x])

    for i, h in enumerate(grid[y][:x][::-1]):
        if h >= check_height:
            left_visible = i + 1
            break
    
    # Trees visible to the right
    if x != len(grid[0]) - 1:
        right_visible = len(grid[y][(x + 1):])
        for i, h in enumerate(grid[y][(x + 1):]):
            if h >= check_height:
                right_visible = i + 1
                break
    else:
        right_visible = 0

    # Trees visible upwards
    up_visible = len(grid[:y])

    for i, row in enumerate(grid[:y][::-1]):
        if row[x] >= check_height:
            up_visible = i + 1
            break

    # Trees visible down
    if y != len(grid) - 1:
        down_visible = len(grid[(y + 1):])
        for i, row in enumerate(grid[(y + 1):]):
            if row[x] >= check_height:
                down_visible = i + 1
                break
    else:
        down_visible = 0

    
    return left_visible * right_visible * up_visible * down_visible

print("Part 1: ", len(set.union(get_left_visible(grid), get_right_visible(grid), get_top_visible(grid), get_bottom_visible(grid))))

print("Part 2: ", max([get_scenic_score(x, y, grid) for y, row in enumerate(grid) for x, _ in enumerate(row)]))
