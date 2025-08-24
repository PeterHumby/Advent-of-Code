
file = open(r"2024/Inputs/Day 12 Input.txt", "r")

data = file.read()
rows = [list(line) for line in data.split('\n')]
grid = [(x, y, p) for y, row in enumerate(rows) for x, p in enumerate(row)]

def get_next_region(grid):
    start = grid[0]
    region = []
    edge = [start]

    while len(edge) > 0:
        region += edge
        for i in range(len(edge)):
            check = edge.pop(0)
            if ((check[0] - 1, check[1], check[2]) not in region) and ((check[0] - 1, check[1], check[2]) not in edge) and ((check[0] - 1, check[1], check[2]) in grid):
                edge.append((check[0] - 1, check[1], check[2]))
            if ((check[0], check[1] - 1, check[2]) not in region) and ((check[0], check[1] - 1, check[2]) not in edge) and ((check[0], check[1] - 1, check[2]) in grid):
                edge.append((check[0], check[1] - 1, check[2]))
            if ((check[0] + 1, check[1], check[2]) not in region) and ((check[0] + 1, check[1], check[2]) not in edge) and ((check[0] + 1, check[1], check[2]) in grid):
                edge.append((check[0] + 1, check[1], check[2]))
            if ((check[0], check[1] + 1, check[2]) not in region) and ((check[0], check[1] + 1, check[2]) not in edge) and ((check[0], check[1] + 1, check[2]) in grid):
                edge.append((check[0], check[1] + 1, check[2]))
    
    return list(set(region))

def area(region):
    return len(region)


def perimiter(region):
    perimiter = 0
    for point in region:
        p = 4
        if (point[0] + 1, point[1], point[2]) in region:
            p -= 1
        if (point[0], point[1] + 1, point[2]) in region:
            p -= 1
        if (point[0] - 1, point[1], point[2]) in region:
            p -= 1
        if (point[0], point[1] - 1, point[2]) in region:
            p -= 1

        perimiter += p
    
    return perimiter

def edge_count(region):
    vertical_edge_points = {} # Points that make up part of a vertical edge, grouped by x coordinate of outer side
    horizontal_edge_points = {} # Points that make up part of a vertical edge, grouped by y coordinate of outer side
    edges = 0

    for point in region:
        if (point[0], point[1] + 1, point[2]) not in region:
            if point[1] + 1 in horizontal_edge_points:
                horizontal_edge_points[point[1] + 1].append(point)
            else:
                horizontal_edge_points[point[1] + 1] = [point]
        if (point[0], point[1] - 1, point[2]) not in region:
            if point[1] - 1 in horizontal_edge_points:
                horizontal_edge_points[point[1] - 1].append(point)
            else:
                horizontal_edge_points[point[1] - 1] = [point]
        if (point[0] + 1, point[1], point[2]) not in region:
            if point[0] + 1 in vertical_edge_points:
                vertical_edge_points[point[0] + 1].append(point)
            else:
                vertical_edge_points[point[0] + 1] = [point]
        if (point[0] - 1, point[1], point[2]) not in region:
            if point[0] - 1 in vertical_edge_points:
                vertical_edge_points[point[0] - 1].append(point)
            else:
                vertical_edge_points[point[0] - 1] = [point]
        
    for y in vertical_edge_points:

        for p in vertical_edge_points[y]:
            if (p[0], p[1] - 1, p[2]) not in vertical_edge_points[y]:
                edges += 1    
        #input("Edges after y=" + str(y) + " = " + str(edges))
    
    for x in horizontal_edge_points:

        for p in horizontal_edge_points[x]:
            if (p[0] - 1, p[1], p[2]) not in horizontal_edge_points[x]:
                edges += 1  
        #input("Edges after x=" + str(x) + " = " + str(edges))
    return edges



tot = 0
while len(grid) > 0:
    region = get_next_region(grid)
    
    for point in region:
        grid.remove(point)
    
    tot += area(region) * edge_count(region)

print(tot)


