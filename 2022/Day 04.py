file = open(r"2022/Inputs/Day 04 Input.txt", "r")

data = file.read().split('\n')

p1_tot, p2_tot = 0, 0
for _, line in enumerate(data):
    A, B = [[int(n) for n in elf.split('-')] for elf in line.split(',')]
    A_range, B_range = set([i for i in range(A[0], A[1] + 1)]), set([j for j in range(B[0], B[1] + 1)])
    
    p1_tot += int((A_range <= B_range) or (B_range <= A_range))
    p2_tot += int(len(A_range.intersection(B_range)) > 0)

print("Part 1: ", p1_tot)
print("part 2: ", p2_tot)