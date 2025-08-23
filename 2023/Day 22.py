file = open(r"2023\Inputs\Day 22 Input.txt", "r")

class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.height = abs(int(z2) - int(z1) + 1)
        self.base = set([(x, y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)])
        self.unremovables = set() # Keep track of which bricks would cause this brick to fall if removed.

class Stack:
    def __init__(self):
        self.height_map = {} # Map of highest brick for (x, y) coordinates in the form (brick, top of brick z-coord)
        self.bricks = []
    
    def add_brick(self, b): # Add a brick to the stack
        self.bricks.append(b)
        under = set(self.height_map.keys()).intersection(b.base) # Check previously seen points below the new brick.
        if not under: # If the base of the brick is clear to the floor, put it on the floor.
            for _, x in enumerate(b.base):
                self.height_map[x] = (b, b.height)
        else: # If the base of the brick is not clear, put it on the maximal supports.
            max_height = max([self.height_map[x][1] for x in under]) # Find the height of the first supports hit
            supports = set([self.height_map[x][0] for x in filter(lambda x: self.height_map[x][1] == max_height, under)]) # Find the bricks at the support height.
            
            if len(supports) == 1: # If only one brick, add that brick and the brick's it is dependant on to unremovables of the new brick.
                support = supports.pop()
                b.unremovables = b.unremovables.union(support.unremovables)
                b.unremovables.add(support)
                
            else: # If more than one brick, add the dependants of all the supporting bricks to unremovables of the new brick as if all fall, the new brick falls too.
                support_unremovables = supports.pop().unremovables.intersection(*[s.unremovables for s in supports])
                b.unremovables = b.unremovables.union(support_unremovables)

            for _, x in enumerate(b.base):
                self.height_map[x] = (b, b.height + max_height)
        
    def count_removables(self):
        return len(set(self.bricks) - set().union(*[b.unremovables for b in self.bricks]))
    
    def get_chain_count(self): 
        count = 0 
        for b in self.bricks: 
            for supp in b.unremovables: 
                count += 1
        return count

stack = Stack()

for _, line in enumerate(sorted(file.read().split('\n'), key=lambda l: int(l.split('~')[0].split(',')[2]))):
    x1, x2 = line.split('~')[0].split(','), line.split('~')[1].split(',')
    line_brick = Brick(*x1, *x2)
    stack.add_brick(line_brick)

print("Part 1: ", stack.count_removables())
print("Part 2: ", stack.get_chain_count())

