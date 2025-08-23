import re
from functools import cache

path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

data = file.read()

towels = data.split('\n\n')[0].split(', ')
towels = sorted(towels, key=lambda x: len(x), reverse=True)
patterns = data.split('\n\n')[1].split('\n')


def cut(pattern, towel): # If possible, remove the given towel from the end of the pattern.
    if len(pattern) == 0:
        return list(pattern)
    if pattern[(-1 * len(towel)):] == towel:
        return pattern[:(-1 * len(towel))]
        
    return pattern


@cache
def check(pattern):
    if len(pattern) == 0:
        return 1
    else:
        outs = []
        for t in towels:
            if re.match(t, pattern):
                outs.append(check(pattern[len(t):]))
        return sum(outs)
    
tot = 0
for p in patterns:
    tot += check(p)

print(tot)