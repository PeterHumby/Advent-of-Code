file = open(r"2024/Inputs/Day 08 Input.txt", "r")

data = [list(line.strip()) for line in file]

nodes = {}

for i in range(len(data)):
    for j in range(len(data[0])):
        if (data[i][j] in nodes) and (data[i][j] != '.'):
            nodes[data[i][j]].append(complex(j, i))
        elif data[i][j] != '.':
            nodes[data[i][j]] = [complex(j, i)]

def gen_antinodes(A, B, data): # Generate the antinodes given complex coordinates of nodes A and B.
    antinodes = [A, B]

    step = (B - A) # Step normalised to real value

    while (0 <= B.real < len(data[0])) and (0 <= B.imag < len(data)):
        B += step
        antinodes.append(B)
    
    while (0 <= A.real < len(data[0])) and (0 <= A.imag < len(data)):
        A -= step
        antinodes.append(A)

    return antinodes

antinodes = []
for freq in nodes:
    node_pairs = list(filter(lambda x: x[0] != x[1], [(A, B) for A in nodes[freq] for B in nodes[freq]]))
    
    for n in node_pairs:
        antinodes += gen_antinodes(n[0], n[1], data)

antinodes = set(filter(lambda n: (0 <= n.real < len(data[0]) and (0 <= n.imag < len(data))), antinodes))

print(len(antinodes))