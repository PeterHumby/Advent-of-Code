import re

file = open(r"2024\Inputs\Day 04 Input.txt", "r")
data = file.read()

lines = data.split('\n')

grid = [list(line) for line in lines] # Wordsearch grid in (row, column) coordinate form
x_coords = [(ind.start(0) // len(lines[0]), ind.start(0) % len(lines[0])) for ind in re.finditer(r'X', ''.join(lines))]
a_coords = [(ind.start(0) // len(lines[0]), ind.start(0) % len(lines[0])) for ind in re.finditer(r'A', ''.join(lines))]

tot = 0

def checkA(grid, x_coord):
    xmas_count = 0
    
    for i in range(-1, 2):
        if 0 <= (x_coord[0] + 3*i) <= (len(lines[0]) - 1):
            for j in range(-1, 2):
                if 0 <= (x_coord[1] + 3*j) <= (len(lines) - 1):
                    if grid[x_coord[0] + i][x_coord[1] + j] == 'M':
                        if grid[x_coord[0] + 2*i][x_coord[1] + 2*j] == 'A':
                            if grid[x_coord[0] + 3*i][x_coord[1] + 3*j] == 'S':
                                xmas_count += 1
    return xmas_count

def checkB(grid, a_coord):

    if (0 < a_coord[0] < (len(lines[0]) - 1)) and (0 < a_coord[1] < (len(lines[0]) - 1)):

        if ((grid[a_coord[0] - 1][a_coord[1] - 1] == "M") and (grid[a_coord[0] + 1][a_coord[1] + 1] == "S")) or ((grid[a_coord[0] - 1][a_coord[1] - 1] == "S") and (grid[a_coord[0] + 1][a_coord[1] + 1] == "M")):
                if ((grid[a_coord[0] + 1][a_coord[1] - 1] == "M") and (grid[a_coord[0] - 1][a_coord[1] + 1] == "S")) or ((grid[a_coord[0] + 1][a_coord[1] - 1] == "S") and (grid[a_coord[0] - 1][a_coord[1] + 1] == "M")):
                        return 1
    return 0

for a_coord in a_coords:
    tot += checkB(grid, a_coord)

print(tot)


