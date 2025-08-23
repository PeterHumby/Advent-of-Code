

path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

blocks = file.read().split('\n\n')

locks = set()
keys = set()

for block in blocks:
    block = block.split('\n')    
    if block[0][0] == '#':
        locks.add('.'.join([str([block[j][i] for j in range(len(block))].count('#') - 1) for i in range(len(block[0]))]))
    else:
        keys.add('.'.join([str([block[j][i] for j in range(len(block))].count('#') - 1) for i in range(len(block[0]))]))

tot = 0

def check(l_heights, k_heights):
    for i in range(len(l_heights)):
        if k_heights[i] + l_heights[i] > 5:
            return False
    return True

for l in locks:
    l_heights = [int(x) for x in l.split('.')]

    for k in keys:
        k_heights = [int(x) for x in k.split('.')]

        if check(l_heights, k_heights):
            tot += 1

print(tot)
