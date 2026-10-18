from functools import reduce
from itertools import combinations

file = open(r"2021/Inputs/Day 08 Input.txt", "r")

patterns = file.read().split('\n')

labels = ['a', 'b', 'c', 'd', 'e', 'f' , 'g']
displays = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9} # Correct mappings for each number

digit_counts = {i: 0 for i in range(10)}
output_sum = 0

def overlay(*bit_patterns): # Give the bitwise xor product of a collection of bit patterns:
    return [reduce(lambda b1, b2: b1 ^ b2, [b[i] for b in bit_patterns]) for i in range(7)]

test_wire_sets = ' '.join(list(displays.keys()))

for _, p in enumerate(patterns):
    mapping_bits = {}
    wire_sets, output = p.split(' | ')
    label_sets = wire_sets.split(' ')
    wire_bits = {n: [int(l in list(n)) for l in labels] for n in label_sets}
    set_sizes = {l: [wire_bits[n] for n in wire_bits if sum(wire_bits[n]) == l] for l in [2, 3, 4, 5, 6, 7]}
    '''
    By uniqueness of segments used, it is clear that:
        - 2 Segments = 1
        - 4 Segments = 4
        - 3 Segments = 7
        - 7 Segments = 8
        - 5 Segments = 2, 3, 5
        - 6 Segments = 0, 6, 9
    '''
    mapping_bits['a'] = overlay(set_sizes[2][0], set_sizes[3][0]) # Overlaying 1 and 7 leaves what maps to 'a'
    
    # Combining 1, 4, 7, and each display using 6 segments will give exactly one bit representation with one segment used - this will be 'g'
    six_segments = sorted([overlay(b, set_sizes[2][0], set_sizes[4][0], set_sizes[3][0]) for b in set_sizes[6]]) 
    mapping_bits['g'] = six_segments.pop(0)

    # Now that 'g' is known, combining 'g', 8, 1, 4, and 7 will leave only 'e'
    mapping_bits['e'] = overlay(mapping_bits['g'], set_sizes[7][0], set_sizes[2][0], set_sizes[4][0], set_sizes[3][0])

    # With 'e' and 'g' removed, the other six segment displays will now only have one bit remaining, this can be checked against 1 to see if they represent 'c' or 'd'
    for check_bit in six_segments:
        check_bit = overlay(check_bit, mapping_bits['e'], mapping_bits['g'])
        if sum(overlay(check_bit, set_sizes[2][0])) == 1:
            mapping_bits['c'] = check_bit
        else:
            mapping_bits['d'] = check_bit
    
    # 1 only consists of 2 bits, 'c' and 'f', so knowing 'c' gives 'f' by default
    mapping_bits['f'] = overlay(set_sizes[2][0], mapping_bits['c'])

    # Knowing all other bits allows 'b' to be found
    mapping_bits['b'] = overlay(set_sizes[4][0], mapping_bits['c'], mapping_bits['d'], mapping_bits['f'])

    mappings = {labels[mapping_bits[seg].index(1)]: seg  for seg in mapping_bits}
    
    pattern_sum = ''
    for num in output.split(' '):
        mapped_digit = displays[''.join(sorted(list(map(lambda c: mappings[c], list(num)))))]
        digit_counts[mapped_digit] += 1
        pattern_sum += str(mapped_digit)
        output_sum += int(pattern_sum)

print("Part 1: ", digit_counts[1] + digit_counts[4] + digit_counts[7] + digit_counts[8])
print("Part 2: ", output_sum)



    
