from itertools import groupby

file = open(r"2025/Inputs/Day 11 Input.txt", "r")

class path:
    def __init__(self, curr, parent=None):
        self.curr = curr
        if parent:  # Parent path to inherit history, default to
            self.dac_visited = parent.dac_visited or (curr == 'dac')
            self.fft_visited = parent.fft_visited or (curr == 'fft')
        else:
            self.dac_visited = (curr == 'dac')
            self.fft_visited = (curr == 'fft')

connections, p1_paths, p2_paths = {}, [path('you')], [path('svr')]

for line in file.read().split('\n'):
    curr, conns = line.split(': ')
    connections[curr] = conns.split(' ')

while len(set([p.curr for p in p1_paths]) - {'out'}) != 0:
    p1_paths = sum([[path(d, p) for d in connections[p.curr]] for p in p1_paths], [])

while len(set([p.curr for p in p2_paths]) - {'out'}) != 0:
    p2_paths = sum([[path(d, p) for d in connections[p.curr]] for p in p2_paths], [])

print("Part 1: ", len(p1_paths))

print("Part 2: ", len(list(filter(lambda p: p.dac_visited and p.fft_visited, paths))))

# nodes = server["you"].connections

# while len(set(nodes) - {"out"}) != 0:
#     nodes = sum([server[n].connections for n in nodes], [])

# print("Part 1: ", len(nodes))

