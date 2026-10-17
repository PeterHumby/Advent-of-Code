file = open(r"2021/Inputs/Day 04 Input.txt", "r")

data = file.read().split('\n\n')

class board:
    def __init__(self, b):
        self.rows = [[int(n) for n in r.split(' ') if n != ''] for r in b.split('\n')] # Seperated integer form row values
        self.h = len(self.rows) # Board height
        self.values = sum(self.rows, []) # All board values
        self.rows, self.cols = [0] * self.h, [0] * self.h
        self.playing = True
    
    def check(self, n): # Check if a value is on the board and if so, does the board have a complete row or column?
        if n not in self.values:
            return 0 # Return no match status
        pos = self.values.index(n)
        x = pos // self.h
        y = pos % self.h
        self.cols[y] += 1
        self.rows[x] += 1
        if (self.h in self.rows) or (self.h in self.cols):
            self.playing = False
            return 2
        return 1

nums = [int(n) for n in data[0].split(',')]
boards = [board(b) for b in data[1:]]
scores = []

for i, n in enumerate(nums):
    for b in boards:
        if b.check(n) == 2:
            scores.append(sum(set(b.values) - set(nums[:i+1])) * n)
    boards = [b for b in boards if b.playing]

print("Part 1: ", scores[0])
print("Part 2: ", scores[-1])

