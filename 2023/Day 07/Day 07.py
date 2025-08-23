path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

data = file.read().split('\n')

hands = {line.split(' ')[0]: int(line.split(' ')[1]) for _, line in enumerate(data)}
tot = 0

def get_strength(hand):

    # # Part 1
    # scores = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}

    # Part 2
    scores = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'T': 'A', 'J': '1', 'Q': 'C', 'K': 'D', 'A': 'E'}

    hex_hand = ''.join(list(map(lambda x: scores[x], list(hand))))
    return int(hex_hand, 16)

def get_max_frequency(hand):
    return max({char: hand.count(char) for char in hand}.values())

def get_max_frequency_subJ(hand):
    hand = ''.join(list(filter(lambda c: c != 'J', list(hand))))

    if len(hand) == 0:
        return 0
    return max({char: hand.count(char) for char in hand}.values())

# # Part 1
# sorted_hands = sorted(hands.keys(), key = lambda h: (5 - len(set(h)), get_max_frequency(h), get_strength(h)))

# Part 2
# hands = {'JJJJJ': 1, 'AAAAJ': 1}

sorted_hands = sorted(hands.keys(), key = lambda h: (5 - len(set(h)) + int('J' in h) - int(set(h) == set('J')), get_max_frequency_subJ(h) + h.count('J'), get_strength(h)))

for rank, h in enumerate(sorted_hands):
    # input((h, (5 - len(set(h)) + int('J' in h), get_max_frequency_subJ(h) + h.count('J'), get_strength(h))))
    tot += (rank + 1) * hands[h]
print(tot)

