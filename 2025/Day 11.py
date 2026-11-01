from functools import cache

file = open(r"2025/Inputs/Day 11 Input.txt", "r")
connections = {line.split(': ')[0]: line.split(': ')[1].split(' ')  for line in file.read().split('\n')}

@cache
def search(start, dac_visited, fft_visited):
    if start == 'out':
        return int(dac_visited and fft_visited)
    return sum([search(branch, dac_visited or start == 'dac', fft_visited or start == 'fft') for branch in connections[start]])

print("Part 1: ", search('you', True, True))
print("Part 2: ", search('svr', False, False))