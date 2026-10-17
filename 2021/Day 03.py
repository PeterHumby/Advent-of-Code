file = open(r"2021/Inputs/Day 03 Input.txt", "r")

lines = file.read().split('\n')


def most_common_bit(lines):
    count = [0] * len(lines[0])
    for l in lines:
        count = [count[i] + int(b == '0') for i, b in enumerate(l)]
    return [str(int(c <= len(lines) // 2)) for c in count]

def least_common_bit(lines):
    return [str(1 - int(b)) for b in most_common_bit(lines)]


gamma_bits = most_common_bit(lines)
epsilon_bits = least_common_bit(lines) # Least common bit

gamma = int(''.join(gamma_bits), 2)
epsilon = int(''.join(epsilon_bits), 2)

print("Part 1: ", gamma * epsilon)

oxy_lines, scrub_lines = lines.copy(), lines.copy()

i = 0
while len(oxy_lines) > 1:
    oxy_lines = [l for l in oxy_lines if l[i] == most_common_bit(oxy_lines)[i]]
    i += 1

i = 0
while len(scrub_lines) > 1:
    scrub_lines = [l for l in scrub_lines if l[i] == least_common_bit(scrub_lines)[i]]
    i += 1

print("Part 2: ", int(oxy_lines[0], 2) * int(scrub_lines[0], 2))
