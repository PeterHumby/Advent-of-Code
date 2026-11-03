file = open(r"2021/Inputs/Day 14 Input.txt", "r")

start, rule_lines = file.read().split('\n\n')

# Mapping of what each pair splits into
rules = {line.split(' -> ')[0]: [line.split(' -> ')[0][0] + line.split(' -> ')[1],  line.split(' -> ')[1] + line.split(' -> ')[0][1]] for line in rule_lines.split('\n')}

pairs = {}
element_counts = {e: start.count(e) for e in set(start)}
for i in range(1, len(start)):
    pairs[start[i-1:i+1]] = pairs.get(start[i-1:i+1], 0) + 1

def step(pairs):
    updated_pairs = {}
    for rule, result in rules.items():
        if rule in pairs:
            count = pairs.pop(rule)
            element_counts[result[0][1]] = element_counts.get(result[0][1], 0) + count
            for p in result:
                updated_pairs[p] = updated_pairs.get(p, 0) + count
    
    for p, count in updated_pairs.items():
        pairs[p] = pairs.get(p, 0) + count
    
    return pairs

for i in range(40):
    pairs = step(pairs)
    print(f"Step {i + 1}: {max(element_counts.values()) - min(element_counts.values())}")

    