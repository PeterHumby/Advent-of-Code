file = open(r"Inputs\Day 02 Input.txt", "r")


def check(report, start):

    if (report[1] == report[0]) and start:
        return check(report[1:], False)

    elif (report[1] == report[0]):
        return 0

    dir = (report[1] - report[0]) // abs(report[1] - report[0])
    accept = [dir, 2*dir, 3*dir]

    for i in range(1, len(report)):
        if report[i] - report[i-1] not in accept:
            if start:
                removed = [check(report[:j] + report[(j+1):], False) for j in range(len(report))]

                if sum(removed) > 0:
                    return 1
                else:
                    return 0

            else:
                return 0
    
    return 1

tot = 0

for line in file:
    line = list(filter(lambda x: x != '', line.strip().split(' ')))

    report = list(map(lambda x: int(x), line))

    if check(report, True) == 0:
        print(report, check(report, True))

    tot += check(report, True)

print(tot)



