

file = open(r"2024\Inputs\Day 05 Input.txt", "r")

conditions = {}
tot = 0


def check(update, conditions, first_pass=True):
    for i in range(len(update)):
            if update[i] in conditions.keys():
                for j in range(i+1, len(update)):
                    if update[j] in conditions[update[i]]:
                        return check(update[:(j-1)] + [update[j], update[j-1]] + update[(j+1):], conditions, first_pass=False)
    if first_pass:
        return 0
    else:
        return int(update[len(update) // 2])

for line in file:
    line = line.strip()
    if '|' in list(line):
        cond = line.split('|')
        if cond[1] in conditions:
            conditions[cond[1]].append(cond[0])
        else:
            conditions[cond[1]] = [cond[0]]
    elif len(line) > 1:
        print(conditions)
        update = line.split(',')
        tot += check(update, conditions)

print(tot)
        
        

