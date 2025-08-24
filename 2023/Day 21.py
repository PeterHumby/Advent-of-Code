file = open(r"2023/Inputs/Day 21 Input.txt", "r")

lines = file.read().split('\n')
w, data = len(lines[0]), ''.join(lines)
start_index = data.index('S')

def expand(edge):
    new_edge = set()
    for p in edge:
        if (((p[0] - 1) // w) == (p[0] // w)):
            new_edge.add((p[0] - 1, p[1]))
        else:
            new_edge.add((((p[0] // w) * w) + w - 1, p[1] - 1))
        if (((p[0] + 1) // w) == (p[0] // w)):
            new_edge.add((p[0] + 1, p[1]))
        else:
            new_edge.add((((p[0] // w) * w), p[1] + 1))
        if (p[0] - w >= 0):
            new_edge.add((p[0] - w, p[1]))
        else:
            new_edge.add((len(data) - w + (p[0] % w), p[1] - 1j))
        if (p[0] + w < len(data)):
            new_edge.add((p[0] + w, p[1]))
        else:
            new_edge.add(((p[0] % w), p[1] + 1j))
    return set(filter(lambda p: data[p[0]] != '#', new_edge))

edge = set([(start_index, 0)]) # Edge points of the form (index, frame) where index is an index in a current frame and frame is a complex coordinate for a given frame.
for i in range(64):
    edge = expand(edge)

print("Part 1: ", len(edge))

'''
26501365 = 65 + (202300 * 131)
Let an 'even' full internal frame match the origin frame and 'odd' match the other full internal frames.

Part 2 solution is based on noticing that the reachable tiles form a diamond made up of alternating copies of reachable frames, 'even' and 'odd' beginning at the original frame.

The diamond is then 'capped' by a distinct point at each vertex and has edges made up of 8 distinct frame types (one more and one less filled type per edge).

The edge and cap frame fill levels are constant for any radius of diamond and so are manually taken for a radius of 2 that can be quickly computed.

The final total can then be found by calculating the number of 'even' and 'odd' filled frames and adding the edge pieces manually.
'''

for i in range(263): # Expand another 263 times for a total of 327 = 65 * (2 * 131) times - i.e. radius 2.
    edge = expand(edge)

fills = {z: len(set(filter(lambda p: p[1] == z, edge))) for z in set([p[1] for p in edge])}

r = 202300 # Diamond radius

even_count = 1 + (4 * ((r - 1) // 2) * (((r - 1) // 2) + 1))
odd_count = 4 * ((r // 2) ** 2)

tot = (even_count * fills[0]) # Internal full 'even' frames
tot += (odd_count * fills[1]) # Internal full 'odd' frames
tot += (r * (fills[-1-2j] + fills[1-2j] + fills[1+2j] + fills[-1+2j])) # External small chunks
tot += ((r - 1) * (fills[1+1j] + fills[-1-1j] + fills[-1+1j] + fills[1-1j])) # External large chunks
tot += (fills[2] + fills[-2] + fills[2j] + fills[-2j]) # Caps

print("Part 2: ", tot)