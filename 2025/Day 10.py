from functools import reduce
from itertools import combinations
from functools import cache
from z3 import *
file = open(r"2025/Inputs/Day 10 Input.txt", "r")

machines = [line.split(' ') for line in file.read().split('\n')]
machines = [[
    tuple([int(M[0][1:-1][i] == '#') for i in range(len(M[0]) - 2)]),
    tuple([tuple([int(i in [int(n) for n in bs[1:-1].split(',')]) for i in range(len(M[0]) - 2)]) for bs in M[1:-1]]),
    tuple([int(n) for n in M[-1][1:-1].split(',')])] for M in machines]

def xor(*bit_sets): # Bitwise xor on a collection of sets of equal length bit sequences
    bit_sets = bit_sets[0]
    return [reduce(lambda b1, b2: b1^b2, [b[i] for b in bit_sets]) for i in range(len(bit_sets[0]))]

def min_presses(target, button_set): # Return the minimum number of button presses needed for a machine to reach its target state.
    target, button_set = list(target), list(button_set)
    for i in range(1, len(button_set) + 1):
        for c_set in combinations(button_set, i):
            if xor(c_set) == target:
                yield c_set

@cache
def configure_voltage(target, button_set): # Return the minimum number of button presses needed for a machine to reach its target state.
    target, button_set = list(target), list(button_set)
    if target == [0]*len(target): # End condition of reaching the target
        return [0]
    
    result = [100000] # Assume the target is unachievable
    parities = [n % 2 for n in target]

    if sum(parities) == 0:
        updated_target = tuple([t // 2 for t in target])
        result += [2*r for r in configure_voltage(updated_target, tuple(button_set))]

    for n in range(1, 2**len(button_set) + 1):
        c_set = [b for i, b in enumerate(button_set) if bin(n)[2:].zfill(len(button_set))[i] == '1']
        if xor(c_set) == parities:
            sum_set = [sum([b[i] for b in c_set]) for i, _ in enumerate(target)]
            updated_target = tuple([(t - sum_set[i]) // 2 for i, t in enumerate(target) if t >= sum_set[i]])

            if len(target) == len(updated_target):
                result += [len(c_set) + 2*r for r in configure_voltage(updated_target, tuple(button_set))]

    if len(result) > 1:
        return result[1:]
    else:
        return result
        
print("Part 1: ", sum([len(next(min_presses(M[0], M[1]))) for M in machines]))


print("Part 2: ", sum([min(configure_voltage(M[2], M[1])) for M in machines]))
