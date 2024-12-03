# PART TWO
import sys

total = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        values = list(map(int, line.split("x")))
        values.sort()
        total += values[0] * values[1] * values[2]
        total += 2 * values[0] + 2 * values[1]

print(total)


# PART ONE
# import sys

# total = 0

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         values = list(map(int, line.split("x")))
#         length, width, height = values[0], values[1], values[2]
#         one = length * width
#         two = width * height
#         three = height * length
#         total += 2 * (one + two + three) + min(one, two, three)

# print(total)