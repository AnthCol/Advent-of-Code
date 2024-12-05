# PART TWO
import sys
from collections import defaultdict


def fix(rules, values):
    copy = values.copy()
    for val in copy:
        after = rules[val]
        index = len(values) - sum(1 for number in after if number in copy) - 1
        values[index] = val

def needs_fix(rules, values):
    for i in range(len(values) - 1):
        remaining = values[i + 1:]
        for val in remaining:
            if val not in rules[values[i]]:
                fix(rules, values)
                return True
    return False


delimiter = '|'
rules = defaultdict(set)

count = 0

with open(sys.argv[1], "r") as f:
    for line in f:

        if line == "\n":
            delimiter = ','
            continue
        
        values = list(map(int, line.strip().split(delimiter)))

        if delimiter == '|':
            rules[values[0]].add(values[1])
        else:
            if needs_fix(rules, values):
                count += values[len(values) // 2]

print(count)


# # PART ONE
# import sys
# from collections import defaultdict

# def check_valid(rules, values):

#     for i in range(len(values) - 1):
#         remaining = values[i + 1:]
#         for val in remaining:
#             if val not in rules[values[i]]:
#                 return False
#     return True


# delimiter = '|'
# rules = defaultdict(set)

# count = 0

# with open(sys.argv[1], "r") as f:
#     for line in f:

#         if line == "\n":
#             delimiter = ','
#             continue
        
#         values = list(map(int, line.strip().split(delimiter)))

#         if delimiter == '|':
#             rules[values[0]].add(values[1])
#         else:
#             if check_valid(rules, values):
#                 count += values[len(values) // 2]

# print(count)


