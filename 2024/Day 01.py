
file = open(r"Inputs\Day 01 Input.txt", "r")

data = file.read().replace('\n', ' ')

data = list(filter(lambda x: x != '', data.split(' ')))

left = [int(data[2*i]) for i in range(len(data) // 2)]

right = [int(data[2*i + 1]) for i in range(len(data) // 2)]

tot = 0

for x in left:
    tot += (x * right.count(x))

print(tot)

