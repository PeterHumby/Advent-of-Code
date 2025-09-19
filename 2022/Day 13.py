import json

file = open(r"2022/Inputs/Day 13 Input.txt", "r")
pairs = [[json.loads(l) for l in p.split('\n')] for p in file.read().split('\n\n')]

def sign(a, b):
    if a == b:
        return 0
    return int((a - b) // ((a - b)**2)**0.5)

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return sign(right, left)

    if isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    if isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    
    if len(left) == 0 and len(right) == 0:
        return 0
    
    if len(left) == 0:
        return 1
    
    if len(right) == 0:
        return -1

    for l, r in zip(left, right):
        result = compare(l, r)
        if result != 0:
            return result

    return sign(len(right), len(left))

print("Part 1: ", sum([i + 1 for i, p in enumerate(pairs) if compare(p[0], p[1]) == 1]))

def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if compare(left[0], right[0]) == 1:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    
    return merged + left + right

pairs.append([[[2]], [[6]]])
packets = sum([p[::compare(*p)] for p in pairs], [])
blocks = [list(b) for b in zip(packets[::2], packets[1::2])]

while len(blocks) > 1:
    if len(blocks) % 2:
        new_blocks = [merge(*b) for b in zip(blocks[::2], blocks[1::2])] + [blocks[-1]]
        blocks = new_blocks
    else:
        blocks = [merge(*b) for b in zip(blocks[::2], blocks[1::2])]

print("Part 2: ", (blocks[0].index([[2]]) + 1) * (blocks[0].index([[6]]) + 1))








