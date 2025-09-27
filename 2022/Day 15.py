from itertools import combinations


file = open(r"2022/Inputs/Day 15 Input.txt", "r")
data = file.read().split('\n')

sensors = [sum([int(coord.split('=')[1]) * ((1j) ** (j)) for j, coord in enumerate(item.split(' at ')[1].split(', '))]) for pair in data for i, item in enumerate(pair.split(': ')) if i % 2 == 0]
beacons = [sum([int(coord.split('=')[1]) * ((1j) ** (j)) for j, coord in enumerate(item.split(' at ')[1].split(', '))]) for pair in data for i, item in enumerate(pair.split(': ')) if i % 2 == 1]

def d(z, w): # Manhattan metric of complex numbers
    return int(abs(z.real - w.real) + abs(z.imag - w.imag))

def sign(a, b):
    if a == b:
        return 0
    return int((a - b) // abs(a - b))

def get_sensor_lines(sensors, dr=0):
    sensor_lines = []
    for i, s in enumerate(sensors):
        r = d(s, beacons[i]) + dr
        sensor_lines.append([
            (s - r * 1j, s + r),
            (s + r, s + r * 1j),
            (s + r * 1j, s - r),
            (s - r, s - r * 1j)])
    return sensor_lines

def get_intersection(l1, l2):
    (x1, y1), (x2, y2) = (l1[0].real, l1[0].imag), (l1[1].real, l1[1].imag)
    (x3, y3), (x4, y4) = (l2[0].real, l2[0].imag), (l2[1].real, l2[1].imag)

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) == 0:
        return None

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    if (min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2)  and min(x3, x4) <= px <= max(x3, x4) and min(y3, y4) <= py <= max(y3, y4)):
        return px + py * 1j
    return None

def get_intersection_points(lines):
    pos_lines = [edge for l in lines for i, edge in enumerate(l) if i in (0, 2)]
    neg_lines = [edge for l in lines for i, edge in enumerate(l) if i in (1, 3)]

    candidates = set()
    for p in pos_lines:
        for n in neg_lines:
            pt = get_intersection(p, n)
            if pt is None:
                continue
            rx, ry = round(pt.real), round(pt.imag)
            if pt.real == rx and pt.imag == ry:
                candidates.add((int(rx), int(ry)))
    return candidates

def check_y(y):
    blocked = set()
    for s in get_sensor_lines(sensors):
        points = y_sensor_intersection(s, y)
        if points:
            left, right = min([int(p.real) for p in points]), max([int(p.real) for p in points])
            for x in range(left, right + 1):
                blocked.add(x + y * 1j)
    return len(blocked - set(beacons) - set(sensors))

def y_line_intersection(l, y):
    l1, l2 = l
    if y > max(l1.imag, l2.imag) or y < min(l1.imag, l2.imag):
        return
    return l1.real + abs(l1.imag - y) * sign(l2.real, l1.real) + y * 1j

def y_sensor_intersection(s, y):
    if y_line_intersection(s[0], y):
        return (y_line_intersection(s[0], y), y_line_intersection(s[3], y))
    elif y_line_intersection(s[1], y):
        return (y_line_intersection(s[1], y), y_line_intersection(s[2], y))
    return False

print("Part 1:", check_y(2000000))

lines = get_sensor_lines(sensors, dr=1)
raw_candidates = get_intersection_points(lines)
limit = 4000000

answer = None
for (x, y) in raw_candidates:
    if not (0 <= x <= limit and 0 <= y <= limit):
        continue
    covered = False
    for s, b in zip(sensors, beacons):
        r = d(s, b)
        if abs(x - s.real) + abs(y - s.imag) <= r:
            covered = True
            break
    if not covered:
        answer = (x, y)
        break

print("Part 2:", x * 4000000 + y)