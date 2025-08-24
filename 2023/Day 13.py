file = open(r"2023/Inputs/Day 13 Input.txt", "r")

blocks = file.read().split('\n\n')

def transpose(block): # Transpose a matrix stored as a list of lists.
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]


    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block

def differences(upper_block, lower_block):
    return sum(u_c != lower_block[j][i] for j, row in enumerate(upper_block) for i, u_c in enumerate(row))
    

def find_symmetries(block):
    height = len(block)
    out = 0
    for i, row in enumerate(block):
        block_height = min([i + 1, height - i - 1])
        upper_block = block[(i - block_height + 1):(i + 1)]
        lower_block = block[(i + 1):(i + block_height + 1)][::-1]

    #     # Part 1
    #     if differences(upper_block, lower_block) == 0:
    #         out += (i + 1)
    # return out - height

        # Part 2
        if differences(upper_block, lower_block) == 1:
            out += (i + 1)
    return out
    
tot = 0
for _, block in enumerate(blocks):
    block = [list(row) for row in block.split('\n')]

    tot += (100 * find_symmetries(block)) + find_symmetries(transpose(block))

print(tot)
