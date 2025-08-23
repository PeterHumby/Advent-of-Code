import time
start_time = time.time()


file = open(r"Inputs\Day 10 Input.txt", "r")

t_map = [['-1'] + list(line.strip()) + ['-1'] for line in file]
t_map.insert(0, (['-1'] * len(t_map[0]))) # Add an upper and lower border to simplify search.
t_map.append((['-1'] * len(t_map[0])))
starts = [(x, y) for y, l in enumerate(t_map) for x, h in enumerate(l) if h == '0']


def get_valid_neighbours(node, t_map):
    neighbours = []
    if int(t_map[node[1] - 1][node[0]]) == int(t_map[node[1]][node[0]]) + 1:
        neighbours.append((node[0], node[1] - 1))
    if int(t_map[node[1] + 1][node[0]]) == int(t_map[node[1]][node[0]]) + 1:
        neighbours.append((node[0], node[1] + 1))
    if int(t_map[node[1]][node[0] - 1]) == int(t_map[node[1]][node[0]]) + 1:
        neighbours.append((node[0] - 1, node[1]))
    if int(t_map[node[1]][node[0] + 1]) == int(t_map[node[1]][node[0]]) + 1:
        neighbours.append((node[0] + 1, node[1]))

    return neighbours

def score(start, t_map, top_level=True):
    end_nodes = []
    nodes = [start]
    while len(nodes) > 0:
        if t_map[nodes[0][1]][nodes[0][0]] == '9':
            end_nodes.append(nodes.pop(0))
        else:
            nodes += get_valid_neighbours(nodes.pop(0), t_map)
    
    return len(end_nodes) # len(set(end_nodes)) for Part 1, len(end_nodes) for Part 2

tot = 0
for start in starts:
    tot += score(start, t_map)

print(tot)
print("Process finished --- %s seconds ---" % (time.time() - start_time))