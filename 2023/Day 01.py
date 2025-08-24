import re

file = open(r"2023/Inputs/Day 01 Input.txt", "r")

data = file.read().replace('\n', ' ')

data = list(filter(lambda x: x != '', data.split(' ')))

string_translation = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


first, second = None, None
total = 0

for line in data:
    # search_pattern = '1|2|3|4|5|6|7|8|9' # Part 1
    search_pattern = '(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))' # Part 2

    search_result = [match.group(1) for match in re.finditer(search_pattern, line)]

    digits = [string_translation[d] for d in search_result]

    total += (digits[0] * 10) + digits[-1]
    
print(total)