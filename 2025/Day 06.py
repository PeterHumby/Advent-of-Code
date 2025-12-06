from itertools import groupby

file = open(r"2025/Inputs/Day 06 Input.txt", "r")

def transpose(block): # Transpose a matrix in the form of a list of lists.
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]

    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block



data = file.read().split('\n')

lines = [list(filter(lambda c: c != '', l.split(' '))) for l in data]




p2_problems = []

problems = transpose(lines) # Transpose the input lines matrix to give lists of each problem and its respective operation.
p1_totals, p2_totals = [], []


# Part 2 Input
p2_values = [''.join(n) for n in transpose(data[:-1])]
p2_problems = []
current = []

for v in p2_values:
    if v.isspace() and current:
        p2_problems.append(current)
        current = []
    else:
        current.append(v)

if current:
    p2_problems.append(current)

def solve(inputs, operation):
    acc = {'+': 0, '*': 1}[operation] # Initialise the solution to the problem as either the additive identity of the multiplicative identity.

    for n in inputs:
        acc = eval(str(acc) + operation + str(int(n)))
    
    return acc

for i, p in enumerate(problems):
    operation = p.pop(-1)
    p1_totals.append(solve(p, operation))
    
    p2_totals.append(solve(p2_problems[i], operation))





print("Part 1: ", sum(p1_totals))
print("Part 2: ", sum(p2_totals))