file = open(r"2022/Inputs/Day 09 Input.txt", "r")

moves = [line.split(' ') for line in file.read().split('\n')]

def update_knot(H, T):
    while T not in [H - 1, H + 1, H - 1j, H + 1j, H - 1 - 1j, H + 1 - 1j, H - 1 + 1j, H + 1 + 1j, H]:
        z = H - T
        if z.real != 0 and z.imag != 0:
            T += (z.real / abs(z.real)) + (z.imag / abs(z.imag))*1j
        elif z.real != 0:
            T += (z.real / abs(z.real))
        elif z.imag != 0:
            T += (z.imag / abs(z.imag))*1j
    return T

def process(moves, K=2):
    knots = [0] * K
    visited = set([0])
    dir_map = {'R': 1, 'U': 1j, 'D': -1j, 'L': -1}

    for m_dir, m_steps in moves:
        for _ in range(int(m_steps)):
            knots[0] += dir_map[m_dir]

            for k in range(1, len(knots)):
                knots[k] = update_knot(knots[k - 1], knots[k])

            visited.add(knots[-1])
    return len(visited)

print("Part 1: ", process(moves, K=2))
print("Part 2: ", process(moves, K=10))


