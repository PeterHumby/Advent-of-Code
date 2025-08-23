
import re

mults = []


with open(r"Inputs/Day 03 Input.txt", "r") as file:
    data = "do()" + file.read() + "don't()"

    #data = "do()_mul(1,1)_do()_mul(2,2)_don't()_mul(3,3)_don't()"

    starts = [s.end(0) for s in re.finditer(r'do\(\)', data)]
    stops = [s.end(0) for s in re.finditer(r'don\'t\(\)', data)]
    

    blocks = []

    while starts != []: # Iterate over instances of don't()
        start = starts[0]
        stops = list(filter(lambda x: x > start, stops))
        stop = stops[0]

        starts = list(filter(lambda x: x > stop, starts))
        blocks.append(data[start:stop])
        
    data = ''.join(blocks)
    for i in range(1, 4):
        for j in range(1, 4):
            mults += re.findall(r'mul\(\d{' + str(i) + r'},\d{' + str(j) + r'}\)', data)

tot = 0
for m in mults:
    vals = m[4:-1].split(',')
    tot += int(vals[0]) * int(vals[1])

print(tot)

