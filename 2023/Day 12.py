import re
from functools import cache

file = open(r"2023/Inputs/Day 12 Input.txt", "r")

data = file.read().split('\n')

@cache
def process(springs, lengths):
    if not lengths:
        return int('#' not in springs)
    if not springs:
        return 0
    
    char, length = springs[0], int(lengths[0])

    def working():
        return process(springs[1:], lengths)

    def broken():
        block = springs[:length].replace('?', '#')

        if block != '#' * length:
            return 0
        
        if len(springs) == length:
            return int(len(lengths) == 1)
        
        if springs[length] in ['.', '?']:
            return process(springs[(length + 1):], lengths[1:])
        else:
            return 0
        
    if char == '.':
        return working()
    if char == '#':
        return broken()
    else:
        return working() + broken()


tot = 0

for _, row in enumerate(data):

    # # Part 1
    # springs = row.split(' ')[0] + '.'
    # lengths = row.split(' ')[1].split(',')
    # Part 2
    springs = '?'.join([row.split(' ')[0]] * 5) + '.'
    lengths = ','.join([row.split(' ')[1]] * 5).split(',')

    tot += process(springs, tuple(lengths))
    

print(tot)