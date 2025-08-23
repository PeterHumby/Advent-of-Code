from functools import cache
import time
start_time = time.time()

file = open(r"Inputs\Day 19 Input.txt", "r")

workflow_rows, part_rows = file.read().split('\n\n')

parts = [{['x', 'm', 'a', 's'][i]: int(c.split('=')[1]) for i, c in enumerate(row[:-1].split(','))} for _, row in enumerate(part_rows.split('\n'))] # Extract parts.

workflows = {row.split('{')[0]: [r.split(':') for r in row.split('{')[1][:-1].split(',')] for _, row in enumerate(workflow_rows.split('\n'))} # Extract workflows.

def process_rule(p, r): # Process the part p for rule r.
    if len(r) == 1:
        return r[0]

    if ('<' in r[0]) and (p[r[0].split('<')[0]] < int(r[0].split('<')[1])):
        return r[1]

    if ('>' in r[0]) and (p[r[0].split('>')[0]] > int(r[0].split('>')[1])):
        return r[1]
    
    return

def process_workflow(p, w): # Process the part p for workflow w.
    i = 0
    outcome = process_rule(p, w[i])
    while (i < len(w)) and (not outcome):
        i += 1
        outcome = process_rule(p, w[i])
    if outcome in workflows:
        return process_workflow(p, workflows[outcome])
    
    return outcome == 'A'

tot = 0

# Part 1
for _, p in enumerate(parts):
    if process_workflow(p, workflows['in']):
        tot += sum(p.values())

print("Part 1: ", tot)

def process_rule_p2(p, r):
    if len(r) == 1:
        return r[0], p, None

    if '<' in r[0]:
        param, bound = r[0].split('<')
        bound = int(bound)
        lower_p, upper_p = p.copy(), p.copy()

        if max(p[param]) < bound:
            return r[1], p, None
        elif min(p[param]) >= bound:
            return r[1], None, p
        else:
            lower_p[param] = range(min(p[param]), bound)
            upper_p[param] = range(bound, max(p[param]) + 1)
            return r[1], lower_p, upper_p

    if '>' in r[0]:
        param, bound = r[0].split('>')
        bound = int(bound)
        lower_p, upper_p = p.copy(), p.copy()

        if max(p[param]) <= bound:
            return r[1], None, p
        elif min(p[param]) > bound:
            return r[1], p, None
        else:
            lower_p[param] = range(min(p[param]), bound + 1)
            upper_p[param] = range(bound + 1, max(p[param]) + 1)
            return r[1], upper_p, lower_p

def process_workflow_p2(p, w): # Process the part p for workflow w.
    success_ranges = []

    next_part = p
    
    for _, r in enumerate(w):
        outcome, success, failure = process_rule_p2(next_part, r)

        if success and (outcome == 'A'):
            success_ranges.append(success)
        elif success and (outcome in workflows):
            success_ranges += process_workflow_p2(success, workflows[outcome])

        if not failure:
            break
        else:
            next_part = failure
    
    return success_ranges

base_part = {'x': range(1,4001), 'm': range(1,4001), 'a': range(1,4001), 's': range(1,4001)}

outcome = process_workflow_p2(base_part, workflows['in'])

tot = 0

for p_range in outcome:
    tot += (len(p_range['x']) * len(p_range['m']) * len(p_range['a']) * len(p_range['s']))

print("Part 2: ", tot)

