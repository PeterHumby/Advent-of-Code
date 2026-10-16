file = open(r"2022/Inputs/Day 17 Input.txt", "r")
jets = file.read().strip()

shapes = [
    {2, 3, 4, 5},
    {3, 2 + 1j, 3 + 1j, 4 + 1j, 3 + 2j},
    {2, 3, 4, 4 + 1j, 4 + 2j},
    {2, 2 + 1j, 2 + 2j, 2 + 3j},
    {2, 2 + 1j, 3, 3 + 1j}]

blocks = set()
step = 0

def push(r, d):
    new_rock = {z + {'>': 1, '<': -1}[d] for z in r}
    if (min(z.real for z in new_rock) >= 0) and (max(z.real for z in new_rock) <= 6) and new_rock.isdisjoint(blocks):
        return new_rock
    return r

def drop(r):
    new_rock = {z - 1j for z in r}
    if new_rock.isdisjoint(blocks) and all(z.imag >= 0 for z in new_rock):
        return new_rock
    return r

def display(blocks, rock=set()): 
    height = max({int(z.imag) for z in blocks.union(rock)}, default=0) 
    for y in range(height, -1, -1): 
        for x in range(7): 
            if x + y*1j in blocks: 
                print('#', end='') 
            elif x + y*1j in rock: 
                print('@', end='') 
            else: 
                print('.', end='') 
        print('\n', end='')

max_height = -1
cache = {}

for s in range(50000):
    # max_height = max([z.imag for z in blocks], default=-1)
    rock = {z + (max_height + 4)*1j for z in shapes[s % 5]}

    if (step % len(jets), s % 5) in cache:
        input((s, (step % len(jets), s % 5), cache[(step % len(jets), s % 5)]))
    else:
        cache[(step % len(jets), s % 5)] = cache.get((step % len(jets), s % 5), []) + [max_height]
        
    while True:
        rock = push(rock, jets[step % len(jets)])
        step += 1
        new_rock = drop(rock)
        if new_rock == rock:
            blocks |= rock
            break
        rock = new_rock
    
    max_height = max(max_height, max([z.imag for z in rock]))


    # if {i + max_height*1j for i in range(7)}.issubset(blocks) and (s % 5 == 4):
    #     print("BASE STATE: ", s)

print(int(max(z.imag for z in blocks) + 1))