from copy import deepcopy


path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

grid = [list(line.strip()) for line in file]

data = ''.join(''.join(row) for row in grid)

start_index = list(data).index('^')

state = (complex(start_index % len(grid[0]), start_index // len(grid[0])), complex(0, -1))

rot = complex(0, 1)

def update(state, grid):
    pos = state[0]
    move = state[1]

    new_pos = state[0] + state[1]
    
    if (new_pos.real < 0) or (new_pos.real > (len(grid[0]) - 1)) or (new_pos.imag < 0) or (new_pos.imag > (len(grid) - 1)):
        return (new_pos, state[1])
    elif grid[int(new_pos.imag)][int(new_pos.real)] == '#':
        return (pos, state[1] * rot)
    else:
        return (new_pos, state[1])



'''
Part 1
visited = []

i = 0
while (0 <= state[0].imag < len(grid)) and (0 <= state[0].real < len(grid[0])):
    visited.append(state[0])
    state = update(state, grid)


print(len(set(visited)))

'''

# Part 2

def check(new_b, grid, state):
    history = []
    if grid[int(new_b.imag)][int(new_b.real)] in ['#', '^']:
        return 0
    
    new_grid = deepcopy(grid)
    new_grid[int(new_b.imag)][int(new_b.real)] = '#'


    
    while (0 <= state[0].imag < len(new_grid)) and (0 <= state[0].real < len(new_grid[0])):
        history.append(state)
        change = update(state, new_grid)

        if change in history:
            return 1
        
        state = update(state, new_grid)
    return 0

tot = 0
for i in range(1,len(grid)):
    for j in range(len(grid[0])):

        print(complex(j, i))
        tot += check(complex(j, i), grid, state)
    

print(tot)
