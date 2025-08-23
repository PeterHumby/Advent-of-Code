from itertools import product
import time
start_time = time.time()

file = open(r"Inputs/Day 23 Input.txt", "r")

connections = {}
groups = []

for line in file:
    comps = line.strip().split('-')
    if comps[0] not in connections:
        connections[comps[0]] = set([comps[1]])
    else:
        if comps[1] not in connections[comps[0]]:
            connections[comps[0]].add(comps[1])

    if comps[1] not in connections:
        connections[comps[1]] = set([comps[0]])
    else:
        if comps[0] not in connections[comps[1]]:
            connections[comps[1]].add(comps[0])


'''
#Part 1
for c1 in connections:
    for c2 in connections[c1]:
            for c3 in connections[c2]:
                if (c1 != c2) and (c1 != c3) and (c2 != c3):
                    if (c1 in connections[c2]) and (c1 in connections[c3]) and (c2 in connections[c1]) and (c2 in connections[c3]) and (c3 in connections[c1]) and (c3 in connections[c2]):
                        permutations = [[c1, c2, c3], [c2, c1, c3], [c3, c1, c2], [c1, c3, c2], [c2, c3, c1], [c3, c2, c1]]
                        if len(list(filter(lambda x: x in permutations, groups))) == 0:
                            if (c1[0] == 't') or (c2[0] == 't') or (c3[0] == 't'):
                                groups.append([c1, c2, c3])
                    

print(len(groups))
print(len(connections.keys()))
'''

# Part 2
def check_connected(comps): # Check if a set of computers is fully connected.
    for c1 in comps:
        for c2 in comps:
            if (c1 != c2) and (c1 not in connections[c2]):
                return False
    return True

def gen_connected_group(c): # Generate the largest possible group beginning from computer c.
    group = connections[c]
    group.add(c)
    cons = [set.intersection(connections[k], set(group)) | {k} for k in group]
    cons = sorted(cons, key=lambda x: len(x), reverse=True)
    for g in cons:
        if check_connected(g):
            return g
    return cons[-1]

group = set()
for comp in connections.keys():
    max_group = gen_connected_group(comp)
    if len(max_group) > len(group):
        group = max_group

print(','.join(sorted(list(group))))

print("--- Part 2: %s seconds ---" % (time.time() - start_time))
