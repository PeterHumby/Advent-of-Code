file = open(r"2025/Inputs/Day 08 Input.txt", "r")

class UnionFind:

    def __init__(self, size):
        self.size = size
        self.parent = [i for i in range(size)]
    
    def find(self, i):

        if self.parent[i] == i:
            return i
        
        return self.find(self.parent[i])
    
    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)

    def get_parts(self):
        parts = {}
        for i in range(self.size):
            root = self.find(i)
            parts[root] = parts.get(root, set()).union({i})
        
        return parts

def dist(b1, b2):
    return ((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2 + (b1[2] - b2[2])**2)**0.5

boxes = {i: tuple(int(c) for c in line.split(',')) for i, line in enumerate(file.read().split('\n'))}
distances = {}
connections = {}
for i in range(0, len(boxes)):
    for j in range(i + 1, len(boxes)):
        distances[(i, j)] = dist(boxes[i], boxes[j])

distances = sorted(distances.items(), key=lambda d: d[1])

UF = UnionFind(len(boxes))

for i in range(1000):
    new_connect = distances[i]
    UF.union(new_connect[0][0], new_connect[0][1])

connected_parts = UF.get_parts().values()
circuit_sizes = sorted([len(c) for c in connected_parts])

print("Part 1: ", circuit_sizes[-1] * circuit_sizes[-2] * circuit_sizes[-3])

new_connect = None
while len(set(tuple(sorted(p)) for p in UF.get_parts().values())) > 1:
    new_connect = distances.pop(i)
    UF.union(new_connect[0][0], new_connect[0][1])

print("Part 2: ", boxes[new_connect[0][0]][0] * boxes[new_connect[0][1]][0])