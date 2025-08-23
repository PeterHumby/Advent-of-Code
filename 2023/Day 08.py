from math import lcm

file = open(r"Inputs\Day 08 Input.txt", "r")

data = file.read().split('\n\n')

path = data[0]
edges = {node.split(' = ')[0]: (node.split(' = ')[1][1:4], node.split(' = ')[1][6:9]) for node in data[1].split('\n')}

def path_length(start):
    i = 0
    current = start
    while current != 'ZZZ':
        current = edges[current][int(path[i % len(path)] == 'R')]
        i += 1
    return i

def path_length_end(start):
    i = 0
    current = start
    while current[2] != 'Z':
        current = edges[current][int(path[i % len(path)] == 'R')]
        i += 1
    return i

# Part 1
current = 'AAA'
print("Part 1: ", path_length('AAA'))

# Part 2
starts = [node for _, node in enumerate(edges.keys()) if node[2] == 'A']
path_lengths = []
for n in starts:
    path_lengths.append(path_length_end(n))

print("Part 2: ", lcm(*path_lengths))
