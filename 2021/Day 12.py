from functools import cache

file = open(r"2021/Inputs/Day 12 Input.txt", "r")

connections = {}

for line in file.read().split('\n'):
    left, right = line.split('-')
    connections[left] = connections.get(left, []) + [right]
    connections[right] = connections.get(right, []) + [left]

def search(start, small_visits, part):
    if start == 'end':
        return 1
    if ord(start[0]) >= ord('a'):
         small_visits[start] = small_visits.get(start, 0) + 1
    # Connections conditions check if c is not a visited small cave, or for part 2 if no small cave has been visited twice
    return sum([search(branch, small_visits.copy(), part) for branch in [c for c in connections[start] if small_visits.get(c, -1) < (part - 1) * (2 - int(max(small_visits.values()) > 1)) and c != 'start']])

print("Part 1: ", search('start', {}, 1))

print("Part 2: ", search('start', {}, 2))

