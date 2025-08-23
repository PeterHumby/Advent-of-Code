path = __file__[:__file__.rfind(__file__[0])] + __file__[0]
file = open(path + "Input.txt", "r")

data = file.read().split('\n')

p1_tot, p2_tot = 0, 0
play_map = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
score_map = {'R': 1, 'P': 2, 'S': 3}
win_map = {'R': 'S', 'P': 'R', 'S': 'P'}
lose_map = {'S': 'R', 'R': 'P', 'P': 'S'}
for _, line in enumerate(data):
    opp, play = line.split(' ')
    opp, play = play_map[opp], play_map[play]
    # Part 1
    p1_tot += score_map[play]
    if play == opp:
        p1_tot += 3
    elif win_map[play] == opp:
        p1_tot += 6

    # Part 2
    if play == 'R':
        p2_tot += score_map[win_map[opp]]
    elif play == 'P':
        p2_tot += score_map[opp] + 3
    elif play == 'S':
        p2_tot += score_map[lose_map[opp]] + 6

print("Part 1: ", p1_tot)
print("Part 2: ", p2_tot)