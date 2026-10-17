file = open(r"2021/Inputs/Day 05 Input.txt", "r")

points = {}
diag_points = {}
for line in file.read().split('\n'):
    p1, p2 = line.split(' -> ')
    x1,y1 = [int(p) for p in p1.split(',')]
    x2,y2 = [int(p) for p in p2.split(',')]

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points[x1 + y*1j] = points.get(x1 + y*1j, 0) + 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[x + y1*1j] = points.get(x + y1*1j, 0) + 1
    else:
        dx, dy = (x2 - x1) // abs(x2 - x1), (y2 - y1) // abs(y2 - y1)
        for k in range(abs(x2 - x1) + 1):
                diag_points[x1 + y1*1j + k*(dx + dy*1j)] = diag_points.get(x1 + y1*1j + k*(dx + dy*1j), 0) + 1

print("Part 1: ", len(list(filter(lambda z: points[z] > 1, points))))

points = {z: points.get(z, 0) + diag_points.get(z, 0) for z in set(points).union(set(diag_points))}

print("Part 2: ", len(list(filter(lambda z: points[z] > 1, points))))