from copy import deepcopy
from math import prod

file = open(r"2022/Inputs/Day 11 Input.txt", "r")



monkeys = [{'items': [int(n) for n in block[1].split(': ')[1].split(', ')],
                'operation': block[2].split(': new = ')[1],
                'test': (int(block[5].split('monkey ')[1]), int(block[4].split('monkey ')[1]), int(block[3].split('by ')[1])),
                'inspected': 0}
            for block in [m.split('\n') for m in file.read().split('\n\n')]]

lcm = prod([m['test'][-1] for _, m in enumerate(monkeys)])

def perform_rounds(M, rounds, part=1):
    for _ in range(rounds):
        for _, monkey in enumerate(M):
            monkey['inspected'] += len(monkey['items'])
            while len(monkey['items']) > 0:
                old = monkey['items'].pop(0)
                old = eval(monkey['operation']) % lcm # Result of the Chinese Remainder Theorem.
                if part == 1:
                    old //= 3
                M[monkey['test'][int(old % monkey['test'][-1] == 0)]]['items'].append(old)
    return M

p1_monkeys = perform_rounds(deepcopy(monkeys), rounds=20, part=1)
p2_monkeys = perform_rounds(deepcopy(monkeys), rounds=10000, part=2)


print("Part 1: ", sorted([m['inspected'] for m in p1_monkeys])[-1] * sorted([m['inspected'] for m in p1_monkeys])[-2])
print("Part 2: ", sorted([m['inspected'] for m in p2_monkeys])[-1] * sorted([m['inspected'] for m in p2_monkeys])[-2])

