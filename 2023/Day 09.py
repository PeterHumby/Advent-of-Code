file = open(r"2023/Inputs/Day 09 Input.txt", "r")

data = file.read().split('\n')

tot = 0

for line_num, line in enumerate(data):
    sequences = [[int(n) for n in line.split(' ')]]
    while set(sequences[-1]) != set([0]):
        last_seq = sequences[-1]
        sub_seq = [last_seq[i + 1] - last_seq[i] for i in range(len(last_seq) - 1)]
        sequences.append(sub_seq)

    # # Part 1
    # tot += sum([s[-1] for s in sequences])

    # Part 2
    tot += sum([( (-1) ** n) * s[0] for n, s in enumerate(sequences)])

print(tot)