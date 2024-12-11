# PART TWO
import sys
from collections import defaultdict

numbers = defaultdict(int)

with open(sys.argv[1], "r") as f:
    file_numbers = list(map(int, f.read().strip().split()))
    for f in file_numbers:
        numbers[f] += 1

blinks = 75
for _ in range(blinks):
    new = defaultdict(int)

    for n in numbers.keys():
        amount = numbers[n]

        if n == 0:
            new[1] += amount
        elif len(str(n)) % 2 == 0:
            as_string = str(n)
            left = int(as_string[:len(as_string) // 2])
            right = int(as_string[len(as_string) // 2:])
            new[left] += amount
            new[right] += amount
        else:
            value = n * 2024
            new[value] += amount
    numbers = new

print(sum(count for count in numbers.values()))


# PART ONE
# import sys

# with open(sys.argv[1], "r") as f:
#     numbers = list(map(int, f.read().strip().split()))

# blinks = 25

# for _ in range(blinks):
#     new = []
#     for n in numbers:
#         if n == 0:
#             new.append(1)
#         elif len(str(n)) % 2 == 0:
#             as_string = str(n)
#             left = int(as_string[:len(as_string) // 2])
#             right = int(as_string[len(as_string) // 2:])
#             new.extend([left, right])
#         else:
#             new.append(n * 2024)
#     numbers = new

# print(len(numbers))