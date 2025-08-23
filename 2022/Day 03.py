file = open(r"2022\Inputs\Day 03 Input.txt", "r")

data = file.read().split('\n')

priority = {c: p + 1 for p, c in enumerate(list(map(chr, range(ord('a'), ord('z')+1))) + list(map(chr, range(ord('A'), ord('Z')+1))))}

p1_tot, p2_tot = 0, 0

mem = []

for i, rucksack in enumerate(data):
    mem.append(set(rucksack))
    left, right = rucksack[:(len(rucksack) // 2)], rucksack[(len(rucksack) // 2):]

    overlaps = set(left).intersection(set(right))

    p1_tot += sum([priority[c] for c in overlaps])

    if (i + 1) % 3 == 0:
        p2_tot += priority[mem[0].intersection(mem[1]).intersection(mem[2]).pop()]
        mem = []

print("Part 1: ", p1_tot)
print("Part 2: ", p2_tot)

