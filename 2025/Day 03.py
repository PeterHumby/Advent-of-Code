file = open(r"2025/Inputs/Day 03 Input.txt", "r")


def bestCombination(n, bank): # Find the highest combination of n digits present in a bank.
    digits = []
    while len(digits) < n:
        if len(digits) == n - 1:
            digits.append(str(max(set(int(d) for d in bank))))
        else:
            digits.append(str(max(set(int(d) for d in bank[:-1*(n - len(digits) - 1)]))))
            bank = bank[bank.index(digits[-1]) + 1:]
    return int(''.join(digits))

p1_acc, p2_acc = 0, 0

for _, bank in enumerate(file.read().split('\n')):
    p1_acc += bestCombination(2, bank)
    p2_acc += bestCombination(12, bank)
    


print("Part 1: ", p1_acc)
print("Part 2: ", p2_acc)

        
                