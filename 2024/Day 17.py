
from copy import deepcopy
import time
start_time = time.time()
file = open(r"Inputs/Day 17 Input.txt", "r")

registers = []
queue = []

def combo(lit_operand, registers):
    if lit_operand < 4:
        return lit_operand
    elif 4 <= lit_operand < 7:
        return registers[lit_operand - 4]
    else:
        print("COMBO OPERAND FAILED")
    

def adv(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    com_operand = combo(lit_operand, registers)
    registers[0] = (registers[0] // (2 ** com_operand))
    return pointer + 2, queue, registers, output

def bxl(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    registers[1] = (registers[1] ^ lit_operand)
    return pointer + 2, queue, registers, output

def bst(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    com_operand = combo(lit_operand, registers)
    registers[1] = com_operand % 8
    return pointer + 2, queue, registers, output

def jnz(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    if registers[0] != 0:
        pointer = lit_operand    
        return pointer, queue, registers, output
    else:
        return pointer + 2, queue, registers, output

def bxc(pointer, queue, registers, output):
    registers[1] = (registers[1] ^ registers[2])
    return pointer + 2, queue, registers, output

def out(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    com_operand = combo(lit_operand, registers)
    output.append(com_operand % 8)
    return pointer + 2, queue, registers, output

def bdv(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    com_operand = combo(lit_operand, registers)
    registers[1] = (registers[0] // (2 ** com_operand))
    return pointer + 2, queue, registers, output

def cdv(pointer, queue, registers, output):
    lit_operand = queue[pointer + 1]
    com_operand = combo(lit_operand, registers)
    registers[2] = (registers[0] // (2 ** com_operand))
    return pointer + 2, queue, registers, output

def process(queue, registers):
    output = []
    pointer = 0
    while pointer < len(queue):
        pointer, queue, registers, output = op_codes[queue[pointer]](pointer, queue, registers, output)
    return output

op_codes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

for line in file:
    line = line.strip()
    if (len(line) > 0) and (line.split(':')[0][0] == 'R'):
        registers.append(int(line.split(':')[1][1:]))

    elif (len(line) > 0) and (line.split(':')[0][0] == 'P'):

        queue = [int(x) for x in line.split(':')[1][1:].split(',')]

target = ','.join([str(x) for x in queue])

def check(i, j=len(queue) - 1):

    if process(queue, [i, 0, 0])[0] != queue[j]:
        return

    if j == 0:
        outs.append(i)
    else:
        for k in range(8):
            check(8*i + k, j - 1)
    

    
outs = []
for i in range(8):
    check(i)

for i in sorted(outs):
    print(i, process(queue, [i, 0, 0]))
    
print("--- %s seconds ---" % (time.time() - start_time))