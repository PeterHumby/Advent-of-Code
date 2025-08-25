file = open(r"2022/Inputs/Day 07 Input.txt", "r")

lines = file.read().split('\n')

class Directory:

    def __init__(self, label, parent=None):
        self.files = []
        self.parent = parent
        self.size = 0

        if self.parent:
            self.label = self.parent.label + '/' + label
        else:
            self.label = label
        
    def addFile(self, file):
        self.files.append(file)
        self.size += file
        if self.parent:
            self.parent.addFile(file)

class Hierarchy:

    def __init__(self):
        self.directories = {}
        self.current_dir = None

    def addDirectory(self, label):
        if self.current_dir:
            self.directories[self.current_dir.label + '/' + label] = Directory(label, parent=self.current_dir)
        else:
            self.directories[label] = Directory(label, parent=self.current_dir)
    
    def cd(self, label):
        if label == '..':
            self.current_dir = self.current_dir.parent
        
        elif self.current_dir:
            if self.current_dir.label + '/' + label in self.directories:
                self.current_dir = self.directories[self.current_dir.label + '/' + label]
            else:
                self.addDirectory(label)
                self.current_dir = self.directories[self.current_dir.label + '/' + label]
        else:
            if label in self.directories:
                self.current_dir = self.directories[label]
            else:
                self.addDirectory(label)
                self.current_dir = self.directories[label]

hierarchy = Hierarchy()

for _, line in enumerate(lines):
    if line[:4] == '$ cd': # Change directory logic
        hierarchy.cd(line[5:])
    elif line[:3] == 'dir': # New directory logic
        hierarchy.addDirectory(line[4:])
    elif line[:4] != '$ ls': # File logic
        file_size, file_label = line.split(' ')
        hierarchy.current_dir.addFile(int(file_size))

for d in hierarchy.directories:
    print(d, hierarchy.directories[d].size)

print("Part 1: ", sum([hierarchy.directories[d].size for d in hierarchy.directories if hierarchy.directories[d].size <= 100000]))

print("Part 2: ", min([hierarchy.directories[d].size for d in hierarchy.directories if 70000000 - hierarchy.directories['/'].size + hierarchy.directories[d].size >= 30000000]))

