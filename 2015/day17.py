# PART TWO
import sys

minimum = sys.maxsize

def generate_combos(sizes, combo, index, combinations):
    litres = sum(combo) 

    if litres > 150:
        return
    if litres == 150:
        global minimum
        minimum = min(minimum, len(combo))
        combinations.append(combo.copy())
        return

    if index == len(sizes):
        return

    generate_combos(sizes, combo, index + 1, combinations)

    copy = combo.copy()
    copy.append(sizes[index])
    generate_combos(sizes, copy, index + 1, combinations)

sizes = []
with open(sys.argv[1], "r") as f:
    for line in f:
        sizes.append(int(line.strip()))

combinations = []
generate_combos(sizes, [], 0, combinations)

count = 0
for c in combinations:
    if len(c) == minimum:
        count += 1
print(count)


# PART ONE
# import sys

# count = 0

# def generate_combos(sizes, combo, index):
#     litres = sum(combo) 

#     if litres > 150:
#         return
#     if litres == 150:
#         global count
#         count += 1
#         return

#     if index == len(sizes):
#         return

#     generate_combos(sizes, combo, index + 1)

#     copy = combo.copy()
#     copy.append(sizes[index])
#     generate_combos(sizes, copy, index + 1)

# sizes = []
# with open(sys.argv[1], "r") as f:
#     for line in f:
#         sizes.append(int(line.strip()))

# generate_combos(sizes, [], 0)


# print(count)
