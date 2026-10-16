file = open(r"2021/Inputs/Day 02 Input.txt", "r")

p1_pos, p2_pos, aim = 0, 0, 0
dirs = {'forward': (1, 0), 'down': (1j, 0), 'up': (-1j, )}

for line in file.read().split('\n'):
    d, dv = line.split()

    if d == 'up':
        p1_pos -= int(dv)*1j
        aim -= int(dv)

    elif d == 'down':
        p1_pos += int(dv)*1j
        aim += int(dv)

    elif d == 'forward':
        p1_pos += 1*int(dv)
        p2_pos += 1*int(dv)
        p2_pos += aim*int(dv)*1j
    
print("Part 1: ", int(p1_pos.real * p1_pos.imag))
print("Part 2: ", int(p2_pos.real * p2_pos.imag))