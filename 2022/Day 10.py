file = open(r"2022/Inputs/Day 10 Input.txt", "r")


check_cycles = [20, 60, 100, 140, 180, 220]

cycles = {0: 1}
curr_cycle = 1
x = 1

for line in file.read().split('\n'):
    if line[:5] == 'addx ':
        v = int(line[5:])
        cycles |= {curr_cycle: x, curr_cycle + 1: x}
        x += v
        curr_cycle += 2
    else:
        cycles |= {curr_cycle: x}
        curr_cycle += 1

print("Part 1: ", sum([c * cycles[c] for c in check_cycles]))

def display(cycles):
    for c in cycles:

        if cycles[c] + 1 in range((c % 40) - 1, (c % 40) + 2):
            print('#', end='')
        else:
            print('.', end='')
        if c % 40 == 0:
            print('\n', end='')

display(cycles)