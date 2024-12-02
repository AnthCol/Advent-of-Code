# PART TWO
import sys

def check(nums):
    index = 0
    inc = True
    dec = True
    while (inc or dec) and index != len(nums) - 1:
        one = nums[index]
        two = nums[index + 1]

        if two - one not in [1, 2, 3]:
            inc = False
        if one - two not in [1, 2, 3]:
            dec = False

        index += 1

    return inc or dec


safe_count = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        numbers = list(map(int, line.split()))

        if check(numbers):
            safe_count += 1
        else: 
            lists = [numbers[:i] + numbers[i + 1:] for i in range(len(numbers))]
            for l in lists:
                if check(l):
                    safe_count += 1
                    break 

print(safe_count)


# PART ONE
# import sys

# def check(nums):
#     index = 0
#     inc = True
#     dec = True
#     while (inc or dec) and index != len(nums) - 1:
#         one = nums[index]
#         two = nums[index + 1]

#         if two - one not in [1, 2, 3]:
#             inc = False
#         if one - two not in [1, 2, 3]:
#             dec = False

#         index += 1


#     return inc or dec


# safe_count = 0

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         numbers = list(map(int, line.split()))
#         safe_count += 1 if check(numbers) else 0

# print(safe_count)