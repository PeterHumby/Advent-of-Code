file = open(r"2021/Inputs/Day 10 Input.txt", "r")

lines = [list(l) for l in file.read().split('\n')]

open_brackets = ['{', '[', '(', '<']
open_map = {'{': '}', '[': ']', '(': ')', '<': '>'}
close_map = {'}': '{', ']': '[', ')': '(', '>': '<'}
p1_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
p2_points = {')': 1, ']': 2, '}': 3, '>': 4}


def check_line(l): # Return the condition of a line, 0
    check_queue = []

    for i, b in enumerate(l):
        if b in open_brackets:
            check_queue.append(b)
        elif len(check_queue) == 0:
            return True, p1_points[b]
        elif check_queue.pop(-1) != close_map[b]:
            return True, p1_points[b]
    
    return False, [open_map[b] for b in check_queue]
        
p1_sum = 0
p2_scores = []

for l in lines:
    p2_sum = 0
    corrupted, result = check_line(l)

    if corrupted:
        p1_sum += result
    else:
        for b in result[::-1]:
            p2_sum *= 5
            p2_sum += p2_points[b]
        p2_scores.append(p2_sum)




print("Part 1: ", p1_sum)
print("Part 2: ", sorted(p2_scores)[len(p2_scores) // 2])

    


    
