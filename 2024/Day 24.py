from copy import deepcopy

file = open(r"Inputs/Day 24 Input.txt", "r")
data = file.read().split('\n\n')

def XOR(a, b):
    return a ^ b

def AND(a, b):
    return (a + b) // 2

def OR(a, b):
    if a or b:
        return 1
    return 0
    
wires = {}
operations = []

for line in data[0].split('\n'):
    wires[line.split(': ')[0]] = int(line.split(': ')[1])

for line in data[1].split('\n'):
    op = (line.split(' -> ')[0][:3], line.split(' -> ')[0][-3:], line.split(' -> ')[0][4:-4], line.split(' -> ')[1])
    operations.append(op)
        
ops = deepcopy(operations)

while len(operations) > 0:
    for op in operations:
        if (op[0] in wires) and (op[1] in wires):
            wires[op[3]] = globals()[op[2]](wires[op[0]], wires[op[1]])
            operations.remove(op)

out = []
for w in wires:
    if w[0] == 'z':
        out.append((int(w[1:]), wires[w]))


'''
Part 1
out = sorted(out, key=lambda x: x[0])

result = sum([x[1] * (2**x[0]) for x in out])

print(result)
'''



wrong = set()
for op1, op2, op, res in ops:
    if res[0] == "z" and op != "XOR" and res != "z45":
        wrong.add(res)
    if (op == "XOR") and (res[0] not in ["x", "y", "z"]) and (op1[0] not in ["x", "y", "z"]) and (op2[0] not in ["x", "y", "z"]):
        wrong.add(res)
    if (op == "AND") and ("x00" not in [op1, op2]):
        for subop1, subop2, subop, subres in ops:
            if ((res == subop1) or (res == subop2)) and (subop != "OR"):
                wrong.add(res)
    if op == "XOR":
        for subop1, subop2, subop, subres in ops:
            if ((res == subop1) or (res == subop2)) and (subop == "OR"):
                wrong.add(res)



print(','.join(sorted(wrong)))
