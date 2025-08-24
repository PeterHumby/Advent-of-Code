import re

file = open(r"2023/Inputs/Day 02 Input.txt", "r")

data = list(filter(lambda x: x != '', file.read().split('\n')))

colour_limits = {'red': 12, 'green': 13, 'blue': 14}

total = 0
'''
# Part 1
for line in data:

    possible = True

    game = line.split(': ')
    draws = game[1].split('; ')
    for draw in draws:
        colours = draw.split(', ')
        if possible:
            for c in colours:
                c = c.split(' ')
                if colour_limits[c[1]] < int(c[0]):
                    possible = False
                    break
        else:
            break
    
    if possible:
        total += int(game[0].split(' ')[1])

print(total)
'''


# Part 2


for line in data:
    max_colours = {'red': 0, 'green': 0, 'blue': 0}

    game = line.split(': ')

    draws = game[1].split('; ')

    for draw in draws:
        colours = draw.split(', ')
        for c in colours:
            c = c.split(' ')
            if max_colours[c[1]] < int(c[0]):
                max_colours[c[1]] = int(c[0])

    total += (max_colours['red'] * max_colours['green'] * max_colours['blue'])

print(total)

