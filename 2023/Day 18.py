file = open(r"2023/Inputs/Day 18 Input.txt", "r")

data = file.read().split('\n')

edge_count = 0
boundary_points = [(0, 0)]
dir_map = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0), '0': (1, 0), '1': (0, 1), '2': (-1, 0), '3': (0, -1)}

for _, row in enumerate(data):
    move = row.split(' ')
    start = boundary_points[-1]

    # # Part 1
    # m_dir, steps = dir_map[move[0]], int(move[1])

    # Part 2
    m_dir, steps = dir_map[move[2][-2]], int(move[2][2:-2], 16)

    boundary_points.append((start[0] + (steps * m_dir[0]), start[1] + (steps * m_dir[1])))
    edge_count += steps

area = 0

for i, v in enumerate(boundary_points):
    area += (((v[0] * boundary_points[(i + 1) % len(boundary_points)][1]) - (v[1] * boundary_points[(i + 1) % len(boundary_points)][0])) / 2) # Shoelace theorem.

print(int(area - (edge_count // 2) + 1 + edge_count))
