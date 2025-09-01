from queue import PriorityQueue

file = open(r"2022/Inputs/Day 12 Input.txt", "r")
data = file.read().split('\n')

S_index, E_index = ''.join(data).index('S'), ''.join(data).index('E')
low_positions = [((i % len(data[0])),  (i // len(data[0]))) for i, c in enumerate(''.join(data)) if c in ['S', 'a']]
S_pos, E_pos = ((S_index % len(data[0])),  (S_index // len(data[0]))), ((E_index % len(data[0])), (E_index // len(data[0])))


grid = [list(line) for line in data]

grid[S_pos[1]][S_pos[0]] = 'a'
grid[E_pos[1]][E_pos[0]] = 'z'

height_map = [[ord(c) for c in line] for line in grid]



curr = None

def get_neighbours(p): # Return the neighbours for the point p = (x, d) where x is the current position and d is the direction used to get there.
    directions = list(filter(lambda d: d != (-1 * p[1][0], -1 * p[1][1]), [(0, 1), (0, -1), (1, 0), (-1, 0)]))
    
    neighbours = [((p[0][0] + d[0], p[0][1] + d[1]), d) for d in directions if (p[0][0] + d[0] in range(len(grid[0]))) and (p[0][1] + d[1] in range(len(grid)))] # Neighbours in bounds.
    neighbours = [n_p for n_p in neighbours if height_map[n_p[0][1]][n_p[0][0]] - height_map[p[0][1]][p[0][0]] <= 1] # Filter by height restriction.

    return neighbours



def shortest_path(start, end):
    costs = {}
    edge = PriorityQueue()
    edge.put((0, (start, (0, 0))))
    while (end not in costs) and (not edge.empty()):
        cost, curr = edge.get()
        cost += 1

        for p in get_neighbours(curr):
            if p[0] not in costs:
                costs[p[0]] = cost
                edge.put((cost, p))

    return costs.get(end, -1)

print("Part 1: ", shortest_path(S_pos, E_pos))

print("Part 2: ", min(list(filter(lambda d: d > 0, [shortest_path(a_pos, E_pos) for a_pos in low_positions]))))





        