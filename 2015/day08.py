# PART TWO
import sys

def encode(string):
    modified = '"\\\"'
    for char in string:
        if char == '\"':
            modified += '\\\"'
        elif char == '\\':
            modified += '\\\\'
        else:
            modified += char
            
    return modified + '\\\"\"'

original = 0
encoded = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        original += len(line.strip())
        line = encode(line.strip()[1:-1])
        encoded += len(line) 


print(encoded - original)

# # PART ONE
# import sys

# literal = 0
# memory = 0

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         line = line.strip()
#         literal += len(line) 
#         line = line[1:-1]

#         mem = 0
#         i = 0
#         while i < len(line):
#             if line[i] == '\\':
#                 if line[i + 1] == 'x':
#                     i += 4
#                 else:
#                     i += 2
#             else:
#                 i += 1 
#             mem += 1
#         memory += mem

# print(literal - memory)
