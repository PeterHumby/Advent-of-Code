file = open(r"2025/Inputs/Day 05 Input.txt", "r")


ranges, ingredients = file.read().split('\n\n')

fresh = [(int(r.split('-')[0]), (int(r.split('-')[1])) + 1) for r in ranges.split('\n')]

acc = 0

for _, ing in enumerate(ingredients.split('\n')):
    for r in fresh:
        if int(ing) in range(r[0], r[1]):
            acc += 1
            break

print("Part 1: ", acc)

def combine_ranges(r1, r2):
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))

fresh = sorted(fresh, key=lambda r: r[1])

for i in range(len(fresh) - 1, 0, -1): # Move backwards through the sorted fresh ranges to combine where they overlap.
    if fresh[i - 1][1] >= fresh[i][0]:
        fresh[i - 1] = combine_ranges(fresh[i - 1], fresh.pop(i))

print("Part 2: ", sum([r[1] - r[0] for r in fresh]))


