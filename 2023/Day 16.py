import time
start_time = time.time()

file = open(r"2023/Inputs/Day 16 Input.txt", "r")

grid = [list(row) for row in file.read().split('\n')]
w, h = len(grid[0]), len(grid)

# Beams are denoted by pairs of complex numbers [x + yi, a + bi] where x + yi is the current position and a + bi is the current direction.

beams = [[0, 1]] # Initialise with a single beam at 0,0 travelling right.


def display(beams):
    beam_dir_map = {1j: '\033[41mV\033[0m', -1j: '\033[41m^\033[0m', 1: '\033[41m>\033[0m', -1: '\033[41m<\033[0m'}
    beam_pos = {b[0]: beam_dir_map[b[1]] for b in beams}
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            print(beam_pos.get(complex(x, y), c), end='')
        print('\n', end='')

def move(beam, curr_tile):
    splitter_map = {-1j: '-', 1j: '-', 1: '|', -1: '|'}
    mirror_map = {(1, '\\'): 1j, (1, '/'): -1j,
                (-1, '\\'): -1j, (-1, '/'): 1j,
                (1j, '\\'): 1, (1j, '/'): -1,
                (-1j, '\\'): -1, (-1j, '/'): 1}

    if curr_tile in ['\\', '/']:
        return [[beam[0] + mirror_map[(beam[1], curr_tile)], mirror_map[(beam[1], curr_tile)]]]
        
    elif curr_tile == splitter_map[beam[1]]:
        return [[beam[0] + (beam[1] * 1j), beam[1] * 1j], [beam[0] + (beam[1] * -1j), beam[1] * -1j]]

    return [[beam[0] + beam[1], beam[1]]]

def process(beams):
    beam_history = set()
    visited = set() # 'Energised' tiles
    while len(beams) > 0: # While there are active beams.
        beams = list(filter(lambda b: (0 <= b[0].real) and (w > b[0].real) and (0 <= b[0].imag) and (h > b[0].imag) and (tuple(b) not in beam_history), beams))
        new_beams = []
        for _, b in enumerate(beams):
            curr, curr_tile = b[0], grid[int(b[0].imag)][int(b[0].real)]
            visited.add(curr)
            beam_history.add(tuple(b))
            new_beams += move(b, curr_tile)
        beams = new_beams
    return len(visited)

# Part 1
print(process([[0, 1]]))

# Part 2
energised = []
for i in range(w):
    energised.append(process([[i, 1j]]))
    energised.append(process([[complex(i, h - 1), -1j]]))

    energised.append(process([[complex(0, i), 1]]))
    energised.append(process([[complex(w - 1, i), -1]]))

print(max(energised))

print("--- Part 2: %s seconds ---" % (time.time() - start_time))

