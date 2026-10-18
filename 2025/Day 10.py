from functools import reduce
from itertools import combinations, combinations_with_replacement

file = open(r"2025/Inputs/Day 10 Input.txt", "r")

machines = [line.split(' ') for line in file.read().split('\n')]

def xor(*bit_sets): # Bitwise xor on a collection of sets of equal length bit sequences
    bit_sets = bit_sets[0]
    return [reduce(lambda b1, b2: b1^b2, [b[i] for b in bit_sets]) for i in range(len(bit_sets[0]))]

def add(*buttons):
    buttons = buttons[0]
    return [reduce(lambda b1, b2: b1 + b2, [b[i] for b in buttons]) for i in range(len(buttons[0]))]

def min_presses(M): # Return the minimum number of button presses needed for a machine to reach its target state.
    N = len(M[0]) - 2
    target = [int(M[0][1:-1][i] == '#') for i in range(N)]
    button_set = [[int(i in [int(n) for n in bs[1:-1].split(',')]) for i in range(N)] for bs in M[1:-1]]
    
    for i in range(1, len(button_set)):
        for c_set in combinations(button_set, i):
            if xor(c_set) == target:
                return i

def configure_voltage(M): # Return the minimum number of button presses needed for a machine to reach its target state.
    N = len(M[0]) - 2
    target = [int(n) for n in M[-1][1:-1].split(',')]
    button_set = [[int(i in [int(n) for n in bs[1:-1].split(',')]) for i in range(N)] for bs in M[1:-1]]
    
    i = min(target)
    while True:
        print(i)
        for c_set in combinations_with_replacement(button_set, i):
            if add(c_set) == target:
                return i
        i += 1
    
print("Part 1: ", sum([min_presses(M) for M in machines]))


print("Part 2: ", sum([configure_voltage(M) for M in machines]))