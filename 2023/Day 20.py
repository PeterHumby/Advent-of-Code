from math import lcm

file = open(r"Inputs\Day 20 Input.txt", "r")

data = file.read()

modules = {} # Store a module as (type, destinations, state)
pulses = [0, 0]
conjunctions = set()

for _, line in enumerate(data.split('\n')):
    module, destinations = line.split(' -> ')
    if '%' in module:
        modules[module[1:]] = ['%', destinations.split(', '), 0]
    elif '&' in module:
        modules[module[1:]] = ['&', destinations.split(', '), {}, {}]
        conjunctions.add(module[1:])
    else:
        modules[module] = ['broadcaster', destinations.split(', ')]

for m in modules:
    for c_input in conjunctions.intersection(set(modules[m][1])):
        modules[c_input][2][m] = 0

def pulse(m, p, src, press_count=None): # Send a pulse 'p' to a module 'm', high = 1, low = 0
    if m not in modules:
        return []

    m_type, destinations, out = modules[m][0], modules[m][1], p
    
    if m_type == '%':
        if not p:
            modules[m][2] += 1
            modules[m][2] %= 2
            out = modules[m][2]
        else:
            return []

    elif m_type == '&':
        if p and (src not in modules[m][3]):
            modules[m][3][src] = press_count
        modules[m][2][src] = p
        if all(modules[m][2].values()):
            out = 0
        else:
            out = 1

    return [(d_m, out, m) for _, d_m in enumerate(destinations)]

def button(press_count=None):
    pulses[0] += 1
    queue = [('broadcaster', 0, None)] # Queue pulses in the form (target, pulse, source).
    found = False
    while queue:
        current = queue.pop(0)
        found = (current[0] == m) and (current[0] == 1)
        new_queue = pulse(*current, press_count)
        for p in new_queue:
            pulses[p[1]] += 1
        queue += new_queue
    return found
    

# # Part 1
# for i in range(1000):
#     button()
# print("Part 1: ", pulses[0] * pulses[1])

# Part 2
press_count = 0
while len(modules['zh'][3]) < len(modules['zh'][2]):
    press_count += 1
    button(press_count)
print("Part 2: ", lcm(*modules['zh'][3].values()))
