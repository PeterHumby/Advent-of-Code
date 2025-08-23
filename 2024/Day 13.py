import time
start_time = time.time()

file = open(r"Inputs\Day 13 Input.txt", "r")

configs = file.read().split('\n\n')

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def parse_config(config):
    lines = config.split('\n')
    lines = [line[(line.index(': ') + 2):].split(', ') for line in lines]
    lines = list(map(lambda x: [int(x[0][2:]), int(x[1][2:])], lines))
    return lines

def row_mult(M, i, m): # Multiply row i of a matrix M by m.

    M[i] = [(int(ent[0] * m[0] / gcd(ent[0] * m[0], ent[1] * m[1])), int(ent[1] * m[1] / gcd(ent[0] * m[0], ent[1] * m[1]))) for ent in M[i]]

    return M

def add_mult_row(M, i, j, m): # Add m * row i to row j.
    M[j] = [(int(((M[i][k][0] * M[j][k][1] * m[0]) + (M[j][k][0] * M[i][k][1] * m[1])) / gcd((M[i][k][0] * M[j][k][1] * m[0]) + (M[j][k][0] * M[i][k][1] * m[1]), M[i][k][1] * M[j][k][1] * m[1])), int((M[i][k][1] * M[j][k][1] * m[1]) / gcd((M[i][k][0] * M[j][k][1] * m[0]) + (M[j][k][0] * M[i][k][1] * m[1]), M[i][k][1] * M[j][k][1] * m[1]))) for k in range(len(M[j]))]
    
    return M

def row_swap(M, i, j): # Swap rows i and j
    M[i], M[j] = M[j], M[i]
    return M


def get_row_lead_count(row):
    check = row[0][0]
    count = 0
    while check == 0:
        count += 1
        check = row[count][0]
    return count

def get_lead_count(M):
    lead_counts = {}
    for i in range(len(M)): # For row in M, taking index
        row = M[i]
        lead_counts[i] = get_row_lead_count(row)
    return lead_counts

def sort_rows(M): # Sort rows by the number of leading zeroes.
    lead_counts = get_lead_count(M)
    i = len(M) - 1 # Start at the bottom
    swaps = []
    while i != 0:
        if lead_counts[i] < lead_counts[i-1]:
            swaps.append(('S', i, i-1))
            row_swap(M, i, i-1)
            lead_counts[i], lead_counts[i-1] = lead_counts[i-1], lead_counts[i]
            i = len(M) - 1
        else:
            i -= 1
    return (M, swaps)

def RREF(M): # Bring a matrix to RREF
    operations = []


    sorted_rows = sort_rows(M)
    M = sorted_rows[0]
    operations += sorted_rows[1]

    for i in range(len(M)):
        row = M[i]
        ind = get_row_lead_count(row)
        operations.append(('M', i, row[ind][::-1]))
        M = row_mult(M, i, row[ind][::-1])
        for j in range(0, len(M)):
            if i != j:
                mult = M[j][ind]
                operations.append(('AM', i, j, (-1*mult[0], mult[1])))
                M = add_mult_row(M, i, j, (-1*mult[0], mult[1]))
    return M, operations

def apply_operations(M, operations):
    for op in operations:
        if op[0] == 'S':
            M = row_swap(M, op[1], op[2])
        elif op[0] == 'M':
            M = row_mult(M, op[1], op[2])
        elif op[0] == 'AM':
            M = add_mult_row(M, op[1], op[2], op[3])
    return M

def frac_add(v, w):
    numerator = int(((w[0] * v[1]) + (w[1] * v[0])) / gcd((w[0] * v[1]) + (w[1] * v[0]), w[1] * v[1]))
    denominator = int((w[1] * v[1]) / gcd((w[0] * v[1]) + (w[1] * v[0]), w[1] * v[1]))

    return (numerator, denominator)

def multiply(M, v):

    prod = []

    for row in M:
        total = (0, 1)

        for i in range(len(row)):
            total = frac_add(total, (int(row[i][0] * v[i][0] / gcd(row[i][0] * v[i][0], row[i][1] * v[i][1])), int(row[i][1] * v[i][1] / gcd(row[i][0] * v[i][0], row[i][1] * v[i][1]))))

        prod.append(total)

    return prod

tot = 0
for config in configs:
    inputs = parse_config(config)
    target = inputs[-1]

    buttons = inputs[:-1]

    buttons = [[(buttons[i][j], 1) for i in range(len(buttons))] for j in range(len(buttons[0]))]
    #target = [(x, 1) for x in target] # Part 1
    target = [(x + 10000000000000, 1) for x in target]
    buttons, operations = RREF(buttons)
    
    identity = [([(0, 1)] * (i)) + [(1, 1)] + ([(0, 1)] * (len(buttons) - i - 1)) for i in range(len(buttons))]
    
    inverse = apply_operations(identity, operations)
    
    solution = multiply(inverse, target)
    
    if (solution[0][0] % solution[0][1] == 0) and (solution[1][0] % solution[1][1] == 0):
        tot += (3 * solution[0][0] // solution[0][1]) + (solution[1][0] // solution[1][1])

print(tot)
print("--- %s seconds ---" % (time.time() - start_time))


