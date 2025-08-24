file = open(r"2024/Inputs/Day 11 Input.txt", "r")

nums = file.read().strip().split(' ')

'''
Part 1
def blink(nums):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == '0':
            nums[i] = '1'
        elif len(nums[i]) % 2 == 0:
            nums.insert(i + 1, str(int(nums[i][((len(nums[i]) // 2)):])))
            nums[i] = nums[i][:((len(nums[i]) // 2))]
        else:
            nums[i] = str(int(nums[i]) * 2024)
    return nums
'''

blink_cache = {}
def blink(n): # Apply a blink to n, getting output a list containing 1 or 2 values.
    n = str(n)

    if n in blink_cache:
        return blink_cache[n]

    if n == '0':
        #blink_cache[n] = ('1', None)
        return ('1', None)
    elif len(n) % 2 == 0:
        #blink_cache[n] = (n[:((len(n) // 2))], str(int(n[((len(n) // 2)):])))
        return (n[:((len(n) // 2))], str(int(n[((len(n) // 2)):])))
    else:
        #blink_cache[n] = (str(int(n) * 2024), None)
        return (str(int(n) * 2024), None)


count_cache = {}
def count(n, blinks):

    if (n, blinks) in count_cache:
        return count_cache[(n, blinks)]

    left, right = blink(n)

    if blinks == 1:
        if right == None:
            #count_cache[(n, blinks)] = 1
            return 1
        else:
            #count_cache[(n, blinks)] = 2
            return 2
    else:
        #out = count(left, blinks - 1)

        if right != None:
            out += count(right, blinks - 1)
        
        #count_cache[(n, blinks)] = out
        return out

tot = 0
for stone in nums:
    print(stone)
    tot += count(stone, 25)

print(tot)