import graphviz
from copy import deepcopy
import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'


path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")
data = file.read().split('\n')

connections = {line.split(': ')[0]: set(line.split(': ')[1].split(' ')) for line in data}

graph = graphviz.Digraph('Day 25 Graph')

graph.engine = 'neato'

for n1 in connections:
    for n2 in connections[n1]:
        graph.edge(n1, n2)

graph.render(directory=path, view=True)

'''

Graph render can be found in repository.

Wires to cut are:
    - kzh <-> rks
    - dgt <-> tnz
    - ddc <-> gqm
'''

def cut_wire(n1, n2): # Cut the wire between two nodes.
    if n1 in connections:
        connections[n1].discard(n2)
    if n2 in connections:
        connections[n2].discard(n1)


cut_wire('kzh', 'rks')
cut_wire('dgt', 'tnz')
cut_wire('ddc', 'gqm')

cut_graph = graphviz.Digraph('Day 25 Cut Graph')

cut_graph.engine = 'neato'

for n1 in connections:
    for n2 in connections[n1]:
        cut_graph.edge(n1, n2)

cut_graph.render(directory=path, view=True)

for n1 in list(connections.keys()):
    for n2 in connections[n1]:
        connections[n2] = connections.get(n2, set()).union(set([n1]))





def flood(n): # Return the number of nodes reachable from a given node.
    edge = set([n])
    visited = edge

    while len(edge) > 0:
        new_edge = set()
        for m in edge:
            new_edge = new_edge.union(set(connections.get(m, [])))
        edge = set(filter(lambda c: c not in visited, new_edge))
        visited = visited.union(edge)

    return len(visited)

print(flood('tgr') * flood('lzl'))
