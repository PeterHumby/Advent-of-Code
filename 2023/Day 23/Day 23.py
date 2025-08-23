
path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

lines = file.read().split('\n')
w = len(lines[0])
grid = ''.join(lines)

edge = [(1, set())] # Store the current head of each path in the form (current index, visited indices)

def adjacents(i, part): # For a given index i, return the valid adjacent indices.

    # Part 1
    if part == 1:
        adjs = [i + w, i - w, i + 1, i - 1]
        if grid[i] in '><^v':
            di = {'^': -1 * w, 'v': w, '>': 1, '<': -1}[grid[i]]
            adjs = [i + di]

    # Part 2
    elif part == 2:
        adjs = [i + w, i - w, i + 1, i - 1]
    

    return set([j for j in adjs if (j in range(len(grid))) and (grid[j] != '#')])

# Depth first search with no repetition on a graph compacted to just vertices.
def search(part):
    verts = set([1, len(grid) - 2])

    for i, c in enumerate(grid):
        if (c != '#') and (len(adjacents(i, part)) > 2):
            verts.add(i)

    # Build a mapping of connections for each vertex and the distance between each connection.
    distances = {}
    connections = {v: [] for v in verts}

    for v in verts:
        visited = set([v]).union(adjacents(v, part))
        edge = adjacents(v, part)

        steps = 1

        while len(edge) > 0:
            for p in edge:
                if p in verts:
                    connections[v].append(p)
                    if steps > distances.get((v, p), 0):
                        distances[(v, p)] = steps
            
            edge = set(filter(lambda p: p not in verts, edge))

            edge = set().union(*[adjacents(p, part) for p in edge]) - visited
            visited = visited.union(edge)

            steps += 1

    v_edge = [(1, [], 0)] # Edge of each path consisting of current vertex and history.
    finished_paths = []

    while len(v_edge) > 0:
        new_edge = []
        for p in v_edge:
            if p[0] == len(grid) - 2:
                finished_paths.append(p[2])
            for q in connections[p[0]]:
                new_edge.append((q, p[1] + [p[0]], p[2] + distances[(p[0], q)]))
        v_edge = list(filter(lambda p: p[0] not in p[1], new_edge))

    return max(finished_paths)

print("Part 1: ", search(1))
print("Part 2: ", search(2))