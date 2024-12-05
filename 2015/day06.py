# PART TWO
import sys
import re


def modify(lights, rows, cols, mode):
    for row in range(rows[0], rows[1] + 1):
        for col in range(cols[0], cols[1] + 1):
            if mode == 'on':
                lights[row][col] += 1
            elif mode == 'off':
                lights[row][col] = max(0, lights[row][col] - 1)
            else:
                lights[row][col] += 2

lights = [[0 for _ in range(1000)] for _ in range(1000)]

with open(sys.argv[1], "r") as f:
    for line in f:
        numbers = list(map(int, re.findall(r'\d+', line)))
        rows = (numbers[0], numbers[2])
        cols = (numbers[1], numbers[3])

        if re.search("on", line):
            modify(lights, rows, cols, 'on')
        elif re.search("off", line):
            modify(lights, rows, cols, 'off')
        else:
            modify(lights, rows, cols, 'toggle')


brightness = 0
for row in lights:
    brightness += sum(col for col in row)

print(brightness)


# # PART ONE
# import sys
# import re


# def modify(lights, rows, cols, mode):
#     for row in range(rows[0], rows[1] + 1):
#         for col in range(cols[0], cols[1] + 1):
#             if mode == 'on':
#                 lights[row][col] = 1
#             elif mode == 'off':
#                 lights[row][col] = 0
#             else:
#                 lights[row][col] ^= 1

# lights = [[0 for _ in range(1000)] for _ in range(1000)]

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         numbers = list(map(int, re.findall(r'\d+', line)))
#         rows = (numbers[0], numbers[2])
#         cols = (numbers[1], numbers[3])

#         if re.search("on", line):
#             modify(lights, rows, cols, 'on')
#         elif re.search("off", line):
#             modify(lights, rows, cols, 'off')
#         else:
#             modify(lights, rows, cols, 'toggle')


# count = 0
# for row in lights:
#     count += sum(1 for col in row if col)

# print(count)