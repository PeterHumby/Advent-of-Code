from functools import cache
from collections import deque


file = open(r"2022/Inputs/Day 16 Input.txt", "r")
data = file.read().split('\n')

tunnels = {}
rates = {}

# Parse input.
for line in data:
    blocks = line.split(' ')
    valve = blocks[1]
    if len(line.split('valves ')) > 1:
        tunnels[valve] = line.split('valves ')[1].split(', ')
    else:
        tunnels[valve] = line.split('valve ')[1].split(', ')
    rates[valve] = int(blocks[4].split('=')[1][:-1])

positive_valves = [v for v in rates if rates[v] > 0] + ["AA"]

bfs_cache = {}

def bfs(start, valves):
    queue = deque([(start, 0)])
    distances = {start: 0}

    key = (start, tuple(valves))

    if key in bfs_cache:
        return bfs_cache[key]

    while queue:
        curr, dist = queue.popleft()
        for next_valve in valves[curr]:
            if next_valve not in distances:
                distances[next_valve] = dist + 1
                queue.append((next_valve, dist + 1))
    
    bfs_cache[key] = distances

    return distances

distances = {}
for valve in positive_valves:
    bfs_result = bfs(valve, tunnels)
    distances[valve] = {v: bfs_result[v] for v in positive_valves if v in bfs_result and v != valve}

dfs_cache = {}


def dfs(current, time, opened): # Depth first search keeping track of current valve, time remaining, open valves, current pressure.
    pressure = 0
    key = (current, time, tuple(sorted(opened)))

    if key in dfs_cache:
        return dfs_cache[key]

    for valve, dist in distances[current].items():
        if (valve not in opened) and (time - dist - 1 > 0):
            valve_released = rates[valve] * (time - dist - 1)
            tot = valve_released + dfs(valve, time - dist - 1, opened | {valve})
            
            pressure = max(pressure, tot)
    
    dfs_cache[key] = pressure
    return pressure

print("Part 1: ", dfs("AA", 30, set()))

multi_dfs_cache = {}

def multi_dfs(curr1, curr2, t1, t2, opened): # DFS algorithm for 2 simultaneous pointers

    key = (tuple(sorted([curr1, curr2])), t1, t2, tuple(sorted(opened)))

    if key in multi_dfs_cache:
        return multi_dfs_cache[key]

    pressure = 0

    if t1 >= t2:
        for valve, dist in distances[curr1].items():
            if (valve not in opened) and (t1 - dist - 1 > 0):
                pressure = rates[valve] * (t1 - dist - 1)
                total = pressure + multi_dfs(valve, curr2, t1 - dist - 1, t2, opened | {valve})
                pressure = max(pressure, total)
    else:
        for valve, dist in distances[curr2].items():
            if (valve not in opened) and (t2 - dist - 1 > 0):
                pressure = rates[valve] * (t2 - dist - 1)
                total = pressure + multi_dfs(curr1, valve, t1, t2 - dist - 1, opened | {valve})
                pressure = max(pressure, total)

    multi_dfs_cache[key] = pressure
    return pressure

print("Part 2:", multi_dfs("AA", "AA", 26, 26, set()))