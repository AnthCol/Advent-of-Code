# PART TWO 
import sys
from collections import defaultdict

nums = []
counts = defaultdict(int)

with open(sys.argv[1], "r") as f:
    for line in f:
        numbers = line.split()
        nums.append(int(numbers[0]))
        counts[int(numbers[1])] += 1

result = sum(num * counts[num] for num in nums)
print(result)




# PART ONE
# import sys

# left = []
# right = []

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         numbers = line.split()
#         left.append(int(numbers[0]))
#         right.append(int(numbers[1]))

# left.sort()
# right.sort()

# dist = sum(abs(l - r) for l, r in zip(left, right))
# print(dist)

