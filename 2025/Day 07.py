file = open(r"2025/Inputs/Day 07 Input.txt", "r")

data = file.read()

beams = {data.index('S'): 1}

splitters = [x + y*1j for y, row in enumerate(data.split('\n')) for x, c in enumerate(row) if c == '^']
last_splitter = max([z.imag for z in splitters])

def progress(beams):
    new_beams = {}
    splits = 0
    for z in beams:
        if z + 1j in splitters:
            splits += 1
            new_beams[z - 1 + 1j] = new_beams.get(z - 1 + 1j, 0) + beams[z]
            new_beams[z + 1 + 1j] = new_beams.get(z + 1 + 1j, 0) + beams[z]
        else:
            new_beams[z + 1j] = new_beams.get(z +1j, 0) + beams[z]
    
    return splits, new_beams

splits = 0
while min([z.imag for z in beams]) <= last_splitter:
    step_splits, beams = progress(beams)
    splits += step_splits

print("Part 1: ", splits)
print("Part 2: ", sum(beams.values()))