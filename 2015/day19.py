# PART TWO
import sys
from collections import defaultdict

minimum = sys.maxsize

def make_string(current, target, steps, rules, leftside):
    if current == target:
        global minimum
        minimum = min(minimum, steps)
        return

    # no rules that replace to something shorter
    if len(current) >= len(target):
        return

    for i in range(len(current)):
        potential_starters = (current[i], current[i:i+2])
        lr_pieces = ((current[:i], current[i+1:]), (current[:i], current[i+2:]))
        for j in range(len(potential_starters)):
            if potential_starters[j] in leftside:
                for replacement in rules[potential_starters[j]]:
                    newstr = ''.join([lr_pieces[j][0], replacement, lr_pieces[j][1]])
                    make_string(newstr, target, steps + 1, rules, leftside)


rules = defaultdict(list)
with open(sys.argv[1], "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) == 3:
            rules[parts[0]].append(parts[2])
        elif parts != []:
            molecule = parts[0]

leftside = set([r for r in rules])
for e_starter in rules['e']:
    make_string(e_starter, molecule, 1, rules, leftside)

print(minimum)


# PART ONE
# import sys
# from collections import defaultdict


# rules = defaultdict(list)
# with open(sys.argv[1], "r") as f:
#     for line in f:
#         parts = line.strip().split()
#         if len(parts) == 3:
#             rules[parts[0]].append(parts[2])
#         elif parts != []:
#             molecule = parts[0]


# leftside = set([r for r in rules])
# distinct = set()

# for i in range(len(molecule)):
#     potential_molecules = (molecule[i], molecule[i:i+2])
#     lr_pieces = ((molecule[:i], molecule[i + 1:]), (molecule[:i], molecule[i + 2:]))

#     for j in range(len(potential_molecules)):
#         if potential_molecules[j] in leftside:
#             for replacement in rules[potential_molecules[j]]:
#                 distinct.add(''.join([lr_pieces[j][0], replacement, lr_pieces[j][1]]))


# print(len(distinct))
