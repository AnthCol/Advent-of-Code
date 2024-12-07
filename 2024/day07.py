# PART TWO
import sys
import re

def make_combos(current_index, max_index, current_perm, perms):
    if current_index == max_index:
        perms.append(current_perm.copy())
        return

    copy = current_perm.copy()
    copy.append('+')
    make_combos(current_index + 1, max_index, copy, perms)
    copy[-1] = '*'
    make_combos(current_index + 1, max_index, copy, perms)
    copy[-1] = '||'
    make_combos(current_index + 1, max_index, copy, perms)


def valid(target, numbers, perms):
    for perm in perms:
        equation = [0] * (len(numbers) + len(perm))
        n, p = 0, 0
        for i in range(len(equation)):
            if i % 2 == 0:
                equation[i] = numbers[n]
                n += 1
            else:
                equation[i] = perm[p]
                p += 1

        val = equation[0]
        for i in range(1, len(equation), 2):
            if equation[i] == '+':
                val += equation[i + 1]
            elif equation[i] == '*':
                val *= equation[i + 1]
            else:
                val = int(str(val) + str(equation[i + 1]))

        if val == target:
            return True

    return False

result = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        numbers = list(map(int, re.findall(r'\d+', line)))
        target = numbers[0]
        numbers = numbers[1:]
        perms = []
        make_combos(0, len(numbers) - 1, [], perms)

        if valid(target, numbers, perms):
            result += target

print(result)


# PART ONE
# import sys
# import re

# def make_combos(current_index, max_index, current_perm, perms):
#     if current_index == max_index:
#         perms.append(current_perm.copy())
#         return

#     copy = current_perm.copy()
#     copy.append('+')
#     make_combos(current_index + 1, max_index, copy, perms)
#     copy[-1] = '*'
#     make_combos(current_index + 1, max_index, copy, perms)


# def valid(target, numbers, perms):
#     for perm in perms:
#         equation = [0] * (len(numbers) + len(perm))
#         n, p = 0, 0
#         for i in range(len(equation)):
#             if i % 2 == 0:
#                 equation[i] = numbers[n]
#                 n += 1
#             else:
#                 equation[i] = perm[p]
#                 p += 1

#         val = equation[0]
#         for i in range(1, len(equation), 2):
#             if equation[i] == '+':
#                 val += equation[i + 1]
#             else:
#                 val *= equation[i + 1]

#         if val == target:
#             return True

#     return False

# result = 0

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         numbers = list(map(int, re.findall(r'\d+', line)))
#         target = numbers[0]
#         numbers = numbers[1:]
#         perms = []
#         make_combos(0, len(numbers) - 1, [], perms)

#         if valid(target, numbers, perms):
#             result += target

# print(result)