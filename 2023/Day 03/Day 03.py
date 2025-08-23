import re

path = __file__[:__file__.rfind('\\')] + '\\'
file = open(path + "Input.txt", "r")

data = file.read()

line_length = data.index('\n')
data_length = len(data)

data = ''.join(data.split('\n'))

nums = {i: int(n.group()) for n in re.finditer(r'\d+', data) for i in range(n.start(), n.end())}
symbol_indices = set([match.start() for match in re.finditer(r'[^0-9.]', data)])


# Part 1
part_nums = []
for index in symbol_indices:
    parts = []
    for k in range(9):
        x_offset, y_offset = (k // 3) - 1, ((k % 3) - 1) * line_length
        if index + x_offset + y_offset in nums.keys():
            parts.append(nums[index + x_offset + y_offset])
    part_nums += list(set(parts))

print(sum(part_nums))



# # Part 2
# tot = 0

# for index in symbol_indices:
#     parts = []
#     for k in range(9):
#         x_offset, y_offset = (k // 3) - 1, ((k % 3) - 1) * line_length
#         if index + x_offset + y_offset in nums.keys():
#             parts.append(nums[index + x_offset + y_offset])
#     parts = list(set(parts))

#     if len(parts) == 2:
#         tot += (parts[0] * parts[1])

# print(tot)