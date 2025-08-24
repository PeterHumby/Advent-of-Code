file = open(r"2022/Inputs/Day 05 Input.txt", "r")

lines, instructions = file.read().split('\n\n')

stack_lines = []

def transpose(block): # Transpose a matrix stored as a list of lists.
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]


    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block

for line in lines.split('\n')[:-1]:
    stack_lines.append([line[1 + 4*i] for i in range((len(line) // 4) + 1)])

S = list(map(lambda s: list(filter(lambda c: c != ' ', s)), transpose(stack_lines)))




def move(stacks, n, a, b, part=1): # Move n crates from stack a to stack b.
    
    if part == 1:
        for _ in range(n):
            stacks[b].insert(0, stacks[a].pop(0))
    elif part == 2:
        move_part = stacks[a][:n]
        stacks[a] = stacks[a][n:]
        stacks[b] = move_part + stacks[b]

    return stacks


def process(stacks, instructions, part=1):
    for _, instruction in enumerate(instructions.split('\n')):
        instruction = instruction.split(' ')
        n = int(instruction[1])
        a = int(instruction[3]) - 1
        b = int(instruction[5]) - 1
        stacks = move(stacks, n, a, b, part)
    
    return stacks

# print("Part 1: ", ''.join([stack[0] for stack in process(S, instructions, part=1)]))

print("Part 2: ", ''.join([stack[0] for stack in process(S, instructions, part=2)]))