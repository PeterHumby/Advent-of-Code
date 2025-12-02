from math import ceil

file = open(r"2025/Inputs/Day 02 Input.txt", "r")

#  if (len(r.split('-')[0]) != len(r.split('-')[1]) or (len(r.split('-')[0]) % 2 == 0))

p1_acc, p2_acc = 0, 0

ranges = [r.split('-') for r in file.read().split(',')]

def block_check(lower, upper, B): # Check for invalid keys with B repeating blocks in the range between lower and upper.
    keys = []

    if len(lower) % B != 0:
        lower = '1' + ('0' * ((B * ceil(len(lower) / B)) - 1) )
    if len(upper) % B != 0:
        upper = '9' * (B * (len(upper) // B))
    
    for n in range(int(lower[:len(lower) // B]), int(upper[:len(upper) // B]) + 1):
        if int(str(n) * B) in range(int(lower), int(upper) + 1):
            keys.append(int(str(n) * B))
    
    return keys

invalid_keys = {}
for _, r in enumerate(ranges):
    for i in range(2, len(r[1]) + 1):
        invalid_keys[i] = invalid_keys.get(i, []) + block_check(r[0], r[1], i)
    
print("Part 1: ", sum(invalid_keys[2]))
print("Part 2: ", sum(set(sum(invalid_keys.values(), []))))
