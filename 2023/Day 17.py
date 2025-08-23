from queue import PriorityQueue

file = open(r"2023\Inputs\Day 17 Input.txt", "r")

grid = [list(line) for line in file.read().split('\n')]

# # Part 1
# min_moves, max_moves = 1, 3

# Part 2
min_moves, max_moves = 4, 10

target = (len(grid[0]) - 1, len(grid) - 1)

costs = {(0, 0): 0}
edge = PriorityQueue()
edge.put((0, ((0, 0), None)))

def get_neighbours(p): # Return the neighbours for the point p = (x, d) where x is the current position and d is the direction used to get there.
    dir_map = {(1, 0): [(0, -1), (0, 1)], (-1, 0): [(0, -1), (0, 1)], (0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)], None: [(-1, 0), (1, 0), (0, -1), (0, 1)]}

    x, d = p[0], p[1]
    new_points = sum([[((x[0] + (n * r_d[0]), x[1] + (n * r_d[1])), r_d) for n in range(min_moves, max_moves + 1)] for r_d in dir_map[d]], [])
    return list(filter(lambda n_p: (n_p[0][0] in range(len(grid[0]))) and (n_p[0][1] in range(len(grid[1]))), new_points))

while not edge.empty():
    cost, curr = edge.get()
    new_points = get_neighbours(curr)

    for p in new_points:
        steps = abs(p[0][0] - curr[0][0]) + abs(p[0][1] - curr[0][1])
        new_cost = cost + sum([int(grid[curr[0][1] + (p[1][1] * n)][curr[0][0] + (p[1][0] * n)]) for n in range(1, steps + 1)])

        if (p not in costs) or (new_cost < costs[p]):
            costs[p] = new_cost
            edge.put((new_cost, p))

target_keys = list(filter(lambda k: k[0] == (len(grid[0]) - 1, len(grid) - 1), costs.keys()))
min_loss = min([costs[k] for k in target_keys])

print(min_loss)


