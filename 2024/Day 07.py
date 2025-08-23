import numpy as np
from copy import deepcopy


file = open(r"2024\Inputs\Day 07 Input.txt", "r")

def process(elements, ops):
    elms = deepcopy(elements)
    run = elms.pop(0)

    for op in ops:
        if op == '0':
            run += elms.pop(0)
        if op == '1':
            run *= elms.pop(0)
        if op == '2':
            run = int(str(run) + str(elms.pop(0)))

    return run
tot = 0


for line in file:
    line = line.strip()
    target = int(line.split(':')[0])
    elements = list(map(lambda x: int(x), line.split(':')[1].split(' ')[1:]))

    op_configs = [list(np.base_repr(n, base=3).zfill(len(elements) - 1))[::-1] for n in range(3**(len(elements) - 1))]

    passed = False
    print(target, elements)
    for ops in op_configs:
        #print(ops, elements, process(elements, ops))
        if (process(elements, ops) == target) and not passed:
            passed = True
            tot += target

print(tot)
