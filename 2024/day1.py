# PART TWO 
import sys
import re 
from collections import defaultdict

nums = []
counts = defaultdict(int)

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.replace('\n', '')
        numbers = re.split('[ ]+', line)
        nums.append(int(numbers[0]))
        counts[int(numbers[1])] += 1


sum = 0
for num in nums:
    sum += num * counts[num]

print(sum)




# PART ONE
# import sys
# import re 

# left = []
# right = []

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         line = line.replace('\n', '')
#         numbers = re.split('[ ]+', line)
#         left.append(int(numbers[0]))
#         right.append(int(numbers[1]))

# left.sort()
# right.sort()

# dist = 0 

# for i in range(len(left)):
#     dist += abs(left[i] - right[i])

# print(dist)

