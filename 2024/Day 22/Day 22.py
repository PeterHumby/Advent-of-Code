from itertools import pairwise

file = open(r"Inputs/Day 22 Input.txt", "r")

def evolve(n):
    n = ( (n << 6) ^ n) % 16777216
    n = ( (n >> 5) ^ n) % 16777216
    n = ( (n << 11) ^ n) % 16777216
    return n

history = {}
for line in file:
    n = int(line.strip())

    prev = n % 10
    prices = [n % 10]
    changes = []
    seen = []
    for i in range(2000):
        n = evolve(n)
        prices.append(n % 10)

    diffs = [b - a for a,b in zip(prices, prices[1:])]

    seen = set()
    for i in range(len(prices)-4):
        changes = tuple(diffs[i:i+4])
        if changes not in seen:
            history[changes] = history.get(changes, 0) + prices[i+4]
            seen.add(changes)
        
print(max(history.values()))