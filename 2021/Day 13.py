file = open(r"2021/Inputs/Day 13 Input.txt", "r")
coords, instructions = file.read().split('\n\n')
dots = set([int(line.split(',')[0]) + int(line.split(',')[1])*1j for line in coords.split('\n')])

def fold_y(fy, dots): # Fold along the y-axis at y = fy
    return {z.real + (fy - (z.imag - fy))*1j if z.imag >= fy else z for z in dots}

def fold_x(fx, dots): # Fold along the y-axis at y = fy
    return {(fx - (z.real - fx)) + z.imag*1j if z.real >= fx else z for z in dots}

for i, inst in enumerate(instructions.split('\n')):
    axis = int(inst.split('=')[1])
    if 'x' in list(inst):
        dots = fold_x(axis, dots)
    else:
        dots = fold_y(axis, dots)

    if i == 0:
        print("Part 1: ", len(dots))

# Part 2 answer is the code displayed after all steps.
print('\n'.join([''.join(['#' if x + y*1j in dots else '.' for x in range(int(max([z.real for z in dots])) + 1)]) for y in range(int(max([z.imag for z in dots])) + 1)]))
