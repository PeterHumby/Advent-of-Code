

file = open(r"Inputs/Day 14 Input.txt", "r")

w=101
h=103
def move(bot, cycles, w, h):
    bot[0][0] = (bot[0][0] + (bot[1][0] * cycles)) % (w)
    bot[0][1] = (bot[0][1] + (bot[1][1] * cycles)) % (h)
    return bot

bots = []
quad_count = [0,0,0,0]


def display(bots):
    grid = [(['.'] * w)] * h
    bot_coords = [b[0] for b in bots]
    
    for i in range(h):
        for j in range(w):
            if [j, i] in bot_coords:
                if j != h:
                    grid[i] = grid[i][:j] + ['#'] + grid[i][(j+1):]
                else:
                    grid[i] = grid[i][:j] + ['#']
    
    for row in grid:
        print(''.join(row))

def mean(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def variance(data):
    N = len(data)
    m = mean(data)
    var = 0
    for i in range(N):
        var += (data[i] - m)**2
    return var / N


for line in file:
    
    bot = [list(map(lambda y: int(y), x[2:].split(','))) for x in line.strip().split(' ')]

    #bot = move(bot, 100, w, h)

    bots.append(bot)

    '''
    Part 1
    if bot[0][0] <= ((w // 2) - 1):
        if bot[0][1] <= ((h // 2) - 1):
            quad_count[0] += 1
        elif bot[0][1] >= ((h // 2) + 1):
            quad_count[1] += 1
    elif bot[0][0] >= ((w // 2) + 1):
        if bot[0][1] <= ((h // 2) - 1):
            quad_count[2] += 1
        elif bot[0][1] >= ((h // 2) + 1):
            quad_count[3] += 1
    '''
i = 0

x_vars, y_vars = [], []





while True:
    x_variance = variance([b[0][0] for b in bots])
    y_variance = variance([b[0][1] for b in bots])

    if (x_variance < mean(x_vars) - 300) and (y_variance < mean(y_vars) - 300):
        print("-------- ", i, " seconds ------------")
        print(x_variance, y_variance)
        display(bots)
        input()

    x_vars.append(x_variance)
    y_vars.append(y_variance)

    bots = [move(bot, 1, w, h) for bot in bots]
    i += 1
