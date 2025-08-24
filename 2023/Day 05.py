file = open(r"2023/Inputs/Day 05 Input.txt", "r")
data = file.read().split('\n\n')

# For each seed, find the min-max source value and check if the seed falls in that range, otherwise 1-1 mapping.

def map_value(source, block):
    ranges = {} # Store the map details corresponding to each source range start
    block = block.split('\n')[1:]
    for _, line in enumerate(block):
        line = line.split(' ')
        ranges[int(line[1])] = (int(line[0]), int(line[1]), int(line[2]))
    
    if source < min(ranges.keys()):
        return source

    min_max = ranges[sorted(list(filter(lambda x: x <= source, ranges.keys())))[-1]]
    dest_start, source_start, span = min_max[0], min_max[1], min_max[2]


    if source < (source_start + span):
        return dest_start + (source - source_start)
    else:
        return source


def map_range(source_range, block):    
    source_start, source_end = source_range[0], source_range[1]

    output_ranges = []
    mappings = {}
    for _, line in enumerate(block.split('\n')[1:]):
        line = line.split(' ')
        
        mappings[int(line[1])] = (int(line[0]), int(line[2]))
    
    effective_mappings = sorted(list(filter(lambda m: 
        (m >= source_start and m <= source_end) or 
        (m + mappings[m][1] - 1 >= source_start and m + mappings[m][1] - 1 <= source_end) or 
        (m <= source_start and m + mappings[m][1] - 1 >= source_end), 
    mappings.keys())))

    if len(effective_mappings) == 0:
        return [source_range]

    for m in effective_mappings:

        if source_start < m:
            output_ranges.append((source_start, m - 1))
            source_start = m

        map_end = min(m + mappings[m][1] - 1, source_end)
        map_offset = mappings[m][0] - m
        output_ranges.append((source_start + map_offset, map_end + map_offset))
        source_start = map_end + 1

    return output_ranges


# # Part 1
# seeds = list(map(lambda x: (int(x), int(x)), data[0].split(': ')[1].split(' ')))

# Part 2
seeds = list(map(lambda x: int(x), data[0].split(': ')[1].split(' ')))
seeds = [(seeds[2*i], seeds[2*i] + seeds[2*i + 1] - 1) for i in range(len(seeds) // 2)]


# input(len(seeds))
test = (43, 98)
for index, block in enumerate(data[1:]):
    new_seeds = []
    for r in seeds:
        new_seeds += map_range(r, block)
    seeds = new_seeds

print(sorted(seeds, key=lambda x: x[0])[0][0])
    
