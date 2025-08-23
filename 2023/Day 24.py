file = open(r"2023\Inputs\Day 24 Input.txt", "r")

stones = file.read().split('\n')


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

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


paths = []
for _, s in enumerate(stones):
    pos, vel = [int(p) for p in s.split(' @ ')[0].split(', ')], [int(v) for v in s.split(' @ ')[1].split(', ')]
    paths.append({'p': {'x': pos[0], 'y': pos[1], 'z': pos[2]}, 'v': {'x': vel[0], 'y': vel[1], 'z': vel[2]}})

tot = 0
check_min, check_max = 200000000000000, 400000000000000
for i, p1 in enumerate(paths):
    for j, p2 in enumerate(paths[(i + 1):]):
        M = [[(p1['v']['x'], 1), (-1*p2['v']['x'], 1)], [(p1['v']['y'], 1), (-1*p2['v']['y'], 1)]]
        v = [(p2['p']['x'] - p1['p']['x'], 1), (p2['p']['y'] - p1['p']['y'], 1)]
        try:
            M_RREF, ops = RREF(M)
            M_INV = apply_operations([[(1, 1),(0, 1)],[(0, 1),(1, 1)]], ops)
            times = multiply(M_INV, v)
            x = (times[0][0] / times[0][1]) * p1['v']['x'] + p1['p']['x']
            y = (times[0][0] / times[0][1]) * p1['v']['y'] + p1['p']['y']
        
            if ((times[0][0] / abs(times[0][0])) == (times[0][1] / abs(times[0][1]))) and ((times[1][0] / abs(times[1][0])) == (times[1][1] / abs(times[1][1]))) and (check_min <= x <= check_max) and (check_min <= y <= check_max):
                tot += 1
        except:
            continue
    

print("Part 1: ", tot)



'''

Example derivation for an equation can be found in github repository.

'''
A, B, C = paths[0], paths[1], paths[2]

M = [[(0, 1), (B['v']['z'] - A['v']['z'], 1), (A['v']['y'] - B['v']['y'], 1), (0, 1), (A['p']['z'] - B['p']['z'], 1), (B['p']['y'] - A['p']['y'], 1)],

[(A['v']['z'] - B['v']['z'], 1), (0, 1), (B['v']['x'] - A['v']['x'], 1), (B['p']['z'] - A['p']['z'], 1), (0, 1), (A['p']['x'] - B['p']['x'], 1)],

[(B['v']['y'] - A['v']['y'], 1), (A['v']['x'] - B['v']['x'], 1), (0, 1), (A['p']['y'] - B['p']['y'], 1), (B['p']['x'] - A['p']['x'], 1), (0, 1)],

[(0, 1), (C['v']['z'] - A['v']['z'], 1), (A['v']['y'] - C['v']['y'], 1), (0, 1), (A['p']['z'] - C['p']['z'], 1), (C['p']['y'] - A['p']['y'], 1)],

[(A['v']['z'] - C['v']['z'], 1), (0, 1), (C['v']['x'] - A['v']['x'], 1), (C['p']['z'] - A['p']['z'], 1), (0, 1), (A['p']['x'] - C['p']['x'], 1)],

[(C['v']['y'] - A['v']['y'], 1), (A['v']['x'] - C['v']['x'], 1), (0, 1), (A['p']['y'] - C['p']['y'], 1), (C['p']['x'] - A['p']['x'], 1), (0, 1)]]


v = [(B['p']['y']*B['v']['z'] - B['p']['z']*B['v']['y'] + A['p']['z']*A['v']['y'] - A['p']['y']*A['v']['z'], 1),

(B['p']['z']*B['v']['x'] - B['p']['x']*B['v']['z'] + A['p']['x']*A['v']['z'] - A['p']['z']*A['v']['x'], 1),

(B['p']['x']*B['v']['y'] - B['p']['y']*B['v']['x'] + A['p']['y']*A['v']['x'] - A['p']['x']*A['v']['y'], 1),

(C['p']['y']*C['v']['z'] - C['p']['z']*C['v']['y'] + A['p']['z']*A['v']['y'] - A['p']['y']*A['v']['z'], 1),

(C['p']['z']*C['v']['x'] - C['p']['x']*C['v']['z'] + A['p']['x']*A['v']['z'] - A['p']['z']*A['v']['x'], 1),

(C['p']['x']*C['v']['y'] - C['p']['y']*C['v']['x'] + A['p']['y']*A['v']['x'] - A['p']['x']*A['v']['y'], 1)]


I = [[(1, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)],
    [(0, 1), (1, 1), (0, 1), (0, 1), (0, 1), (0, 1)],
    [(0, 1), (0, 1), (1, 1), (0, 1), (0, 1), (0, 1)],
    [(0, 1), (0, 1), (0, 1), (1, 1), (0, 1), (0, 1)],
    [(0, 1), (0, 1), (0, 1), (0, 1), (1, 1), (0, 1)],
    [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (1, 1)]]

M_RREF, ops = RREF(M)

M_INV = apply_operations(I, ops)

config = multiply(M_INV, v)

config = [c[0] / c[1] for c in config]

print("Part 2: ", int(config[0] + config[1] + config[2]))
