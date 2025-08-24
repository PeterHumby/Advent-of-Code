file = open(r"2023/Inputs/Day 15 Input.txt", "r")

strings = file.read().split(',')

def HASH(string):
    current = 0

    for _, c in enumerate(string):
        current += ord(c)
        current *= 17
        current %= 256
    
    return current

tot = 0


boxes = {}
for _, string in enumerate(strings):

    # # Part 1
    # tot += HASH(string)

    # Part 2
    if '-' in string:
        label = string.split('-')[0]
        target_box = HASH(label)
        current_box = boxes.get(target_box, {})
        current_box.pop(label, None)

    elif '=' in string:
        label, length = string.split('=')[0], int(string.split('=')[1])
        target_box = HASH(label)
        current_box = boxes.get(target_box, {})
        current_box[label] = length
    
    boxes[target_box] = current_box

for b_i, box in enumerate(boxes.keys()):
    for l_i, lens in enumerate(boxes[box].keys()):
        tot += ((int(box) + 1) * (l_i + 1) * boxes[box][lens])


print(tot)
