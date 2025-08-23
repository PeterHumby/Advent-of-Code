import time
import sys

file = open(r"Inputs\Day 10 Input.txt", "r")

data = file.read().split('\n')

line_length = len(data[0])

animal_index = ''.join(data).index("S")

animal_pos = (animal_index % line_length, animal_index // len(data))

grid = [list(line) for line in data]

inside = []

def display(A_pos, B_pos):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if ((x, y) == A_pos) and ((x, y) == B_pos):
                print("\033[41mC\033[0m", end="")
            elif ((x, y) == A_pos):
                print("\033[41mA\033[0m", end="")
            elif ((x, y) == B_pos):
                print("\033[41mB\033[0m", end="")
            elif grid[y][x] == "S":
                print("\033[41mS\033[0m", end="")
            else:
                print(grid[y][x], end="")
        print("\n\r", end="")
    input()
    



A_steps, B_steps = 1, 1



# Assume the animal is in a valid tube.

def get_starts():
    start_positions = []

    if grid[animal_pos[1] - 1][animal_pos[0]] in ["|", "7", "F"]: # Check for acceptable up move
        start_positions.append((animal_pos[0], animal_pos[1] - 1))
    if grid[animal_pos[1] + 1][animal_pos[0]] in ["|", "L", "J"]: # Check for acceptable down move
        start_positions.append((animal_pos[0], animal_pos[1] + 1))
    if grid[animal_pos[1]][animal_pos[0] + 1] in ["-", "7", "J"]: # Check for acceptable right move
        start_positions.append((animal_pos[0] + 1, animal_pos[1]))
    if grid[animal_pos[1]][animal_pos[0] - 1] in ["-", "L", "F"]: # Check for acceptable left move
        start_positions.append((animal_pos[0] - 1, animal_pos[1]))
    return start_positions[0], start_positions[1]

def get_next_pos(prev_pos, curr_pos):
    curr_type = grid[curr_pos[1]][curr_pos[0]]

    if curr_type in ["-", "|"]:
        return (curr_pos[0] + (curr_pos[0] - prev_pos[0]), curr_pos[1] + (curr_pos[1] - prev_pos[1]))

    elif curr_type == "L":
        if curr_pos[1] == prev_pos[1]:
            
            return (curr_pos[0], curr_pos[1] - 1)
        else:
            return (curr_pos[0] + 1, curr_pos[1])
    
    elif curr_type == "F":
        if curr_pos[1] == prev_pos[1]:
            return (curr_pos[0], curr_pos[1] + 1)
        else:
            return (curr_pos[0] + 1, curr_pos[1])
    
    elif curr_type == "7":
        if curr_pos[1] == prev_pos[1]:
            return (curr_pos[0], curr_pos[1] + 1)
        else:
            return (curr_pos[0] - 1, curr_pos[1])
    
    elif curr_type == "J":
        if curr_pos[1] == prev_pos[1]:
            return (curr_pos[0], curr_pos[1] - 1)
        else:
            return (curr_pos[0] - 1, curr_pos[1])
    
A_pos, B_pos = get_starts()
A_prev, B_prev = animal_pos, animal_pos

A_visited, B_visited = [animal_pos, A_pos], [B_pos]

steps = 1


while A_pos not in [B_pos, B_prev]:
    A_prev, A_pos = A_pos, get_next_pos(A_prev, A_pos)
    B_prev, B_pos = B_pos, get_next_pos(B_prev, B_pos)

    A_visited.append(A_pos)
    B_visited.append(B_pos)

    steps += 1

print(steps)

pieces = A_visited + B_visited[::-1]

for p in pieces:
    if pieces.count(p) > 1:
        pieces.pop(pieces.index(p))

vertices = list(filter(lambda x: grid[x[1]][x[0]] in ['F', 'L', '7', 'S', 'J'], pieces))

area = 0
for i, v in enumerate(vertices):
    area += (((v[0] * vertices[(i + 1) % len(vertices)][1]) - (v[1] * vertices[(i + 1) % len(vertices)][0])) / 2) # Shoelace theorem to calculate area of bounded simple polygon

interior_points = abs(area) - (len(pieces) / 2) + 1 # Pick's theorem to find interior integer points of bounded simple polygon

print(interior_points)