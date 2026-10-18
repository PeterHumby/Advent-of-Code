file = open(r"2021/Inputs/Day 06 Input.txt", "r")
nums = file.read()
fish = {age: nums.count(str(age)) for age in range(9)}

for day in range(257):
    print(day, sum(fish.values()))
    new_fish = {age: fish[age + 1] for age in range(8)}
    new_fish[6] += fish[0]
    new_fish[8] = new_fish.get(8, 0) + fish[0]
    fish = new_fish