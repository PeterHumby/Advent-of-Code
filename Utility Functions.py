

def merge_ranges(ranges): # Merge a list of inclusive ranges stored as tuples in the form (lower_bound, upper_bound).

    def combine_ranges(r1, r2):
        return (min(r1[0], r2[0]), max(r1[1], r2[1]))

    ranges = sorted(ranges, key=lambda r: r[1]) # Sort by upper bounds.

    for i in range(len(ranges) - 1, 0, -1): # Move backwards through the sorted ranges to combine where they overlap.
        if ranges[i - 1][1] >= ranges[i][0]:
            ranges[i - 1] = combine_ranges(ranges[i - 1], ranges.pop(i))
    
    return ranges

def transpose(block): # Transpose a matrix in the form of a list of lists.
    m = len(block)
    n = len(block[0])

    t_block = [[0 for i in range(m)] for i in range(n)]

    for i in range(m):
        for j in range(n):
            t_block[j][i] = block[i][j]
    
    return t_block