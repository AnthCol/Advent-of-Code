# PART TWO
import sys

with open(sys.argv[1], "r") as f:
    content = f.read()

floor = 0
for i in range(len(content)):
    floor += 1 if content[i] == '(' else -1

    if floor == -1:
        print(i + 1)
        break 




# PART ONE
# import sys

# with open(sys.argv[1], "r") as f:
#     content = f.read()

# floor = 0

# for char in content:
#     floor += 1 if char == '(' else -1

# print(floor)
