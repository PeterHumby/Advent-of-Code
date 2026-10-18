file = open(r"2021/Inputs/Day 11 Input.txt", "r")

lines = file.read().split('\n')

w, h = len(lines[0]), len(lines)


energy = [int(n) for n in ''.join(lines)]

def get_neighbours(i): # Get the neighbouring indices around an index i.
    if i % w == 0:
        if i // w == 0:   
            return [i + w, i + 1, i + w + 1]
        elif i // w == h - 1:
            return [i - w, i + 1, i - w + 1]
        else:
            return [i - w, i + w, i + 1, i - w + 1, i + w + 1]
    elif i % w == w - 1:
        if i // w == 0:
            return [i + w, i - 1, i + w - 1]
        elif i // w == h - 1:
            return [i - w, i - 1, i - w - 1]
        else:
            return [i + w, i - w, i - 1, i + w - 1, i - w - 1]
    else:
        if i // w == 0:
            return [i + w, i + 1, i - 1, i + w + 1, i + w - 1]
        elif i // w == h - 1:
            return [i - w, i + 1, i - 1, i - w + 1, i - w - 1]
        else:
            return [i + w, i - w, i + 1, i - 1, i + w + 1, i - w + 1, i + w - 1, i - w - 1]


flash_count = 0
for _ in range(14):
    energy = [n + 1 for n in energy]
 
    flashes = [i for i, e in enumerate(energy) if e >= 10]
    flashed = set()

    while len(flashes) > 0:
        flash_count += len(flashes)
        for i in flashes:
            for j in get_neighbours(i) + [i]:
                energy[j] += 1
            
        flashes = [i for i, e in enumerate(energy) if e >= 10]
    
    energy = [e if e < 10 else 0 for i, e in enumerate(energy)]



