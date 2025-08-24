file = open(r"2023/Inputs/Day 04 Input.txt", "r")
data = file.read().split('\n')

tot = 0
cards = {}

for i, line in enumerate(data):
    line = line.split(' | ')
    winning = set(filter(lambda x: x != '', line[0].split(': ')[1].split(' ')))
    actual = set(filter(lambda x: x != '', line[1].split(' ')))
    
    matches = len(winning.intersection(actual))

    # # Part 1
    # if matches > 0:
    #     tot += (2 ** matches - 1)
    
    cards[i] = [1, matches] # Create a dictionary entry for each card containing the current count of that card and the matches it contains.
for c in cards.keys():
    for i in range(1, cards[c][1] + 1):
        cards[c + i][0] += cards[c][0]

counts = [card[0] for card in cards.values()]

print(sum(counts))