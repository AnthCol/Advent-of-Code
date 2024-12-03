# PART TWO
import sys
import re 

with open(sys.argv[1], "r") as f:
    content = f.read()

total = 0
on = True

for i in range(len(content)):
    remaining = content[i:]
    if remaining.startswith("don't()"):
        on = False
    elif remaining.startswith("do()"):
        on = True
 
    match = re.match(r'mul\(\d+,\d+\)', remaining)

    if on and match:
        mul = match.group(0)
        values = list(map(int, re.findall(r'\d+', mul)))
        total += values[0] * values[1]

print(total)

# # PART ONE
# import sys
# import re 

# with open(sys.argv[1], "r") as f:
#     content = f.read()

# instructions = re.findall(r'mul\(\d+,\d+\)', content)
# total = 0
# for i in instructions:
#     values = list(map(int, re.findall(r'\d+', i)))
#     total += values[0] * values[1]

# print(total)
