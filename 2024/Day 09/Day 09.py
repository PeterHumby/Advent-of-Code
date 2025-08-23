import re


path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

data = file.read()

def gen_disk_map(data):
    data = data + "0"
    disk_map = []
    for i in range(len(data)):
        if i % 2 == 0:
            disk_map += ([str(i // 2)] * int(data[i]))
        else:
            disk_map += (['.'] * int(data[i]))
    return disk_map


def shift(id, disk_map):
    free_blocks = [str(i) for i, x in enumerate(disk_map) if x == '.']
    for i in range(len(free_blocks) - 1, 0, -1):
        if int(free_blocks[i-1]) != int(free_blocks[i]) - 1:
            free_blocks.insert(i, '_')
    free_blocks = list(map(lambda n: list(map(lambda k: int(k), list(filter(lambda m: m != '', n.split('|'))))), ('|'.join(free_blocks)).split('_')))
    target_blocks = [i for i, x in enumerate(disk_map) if x == str(id)]
    for free_block in free_blocks:
        if (len(target_blocks) <= len(free_block)) and (target_blocks[0] > free_block[0]):
            for k in range(len(target_blocks)):
                disk_map[free_block.pop(0)] = str(id)
                disk_map[target_blocks.pop(-1)] = '.'
            return disk_map
    return disk_map

def compact(data):
    disk_map = gen_disk_map(data)

    counts = [data[2*i] for i in range((len(data) // 2) + 1)]
    i = len(counts) - 1

    while (re.findall(r'\d(\.+)\d', ''.join(disk_map)) != []) and (i > 0):
        print(i)
        disk_map = shift(str(i), disk_map)
        i -= 1
    f = open("map.txt", "w")
    f.write(str(disk_map))
    return disk_map



def check_sum(disk_map):
    tot = 0
    for i in range(len(disk_map)):
        if disk_map[i] != '.':
            tot += i * int(disk_map[i])
    return tot


disk_map = compact(data)
print(disk_map)
print(check_sum(disk_map))
