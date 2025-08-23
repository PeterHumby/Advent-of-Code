import os

print(os.listdir("."))
file = open(path + "Input.txt", "r")

data = file.read().split('\n')

for _, rucksack in enumerate(data):
    left = rucksack[:(len(rucksack) // 2)]


print('ABCD'[:(len('ABCD') // 2)])