# PART TWO
import sys

with open(sys.argv[1], "r") as f:
    content = f.read()

x, y = 0, 0
robo_x, robo_y = 0, 0
s = set([(x, y)])
mode = 0

for c in content:
    temp_x, temp_y = 0, 0

    match c:
        case '<':
            temp_x = -1
        case '>':
            temp_x = 1
        case '^':
            temp_y = -1
        case 'v':
            temp_y = 1


    if mode == 0:
        x += temp_x
        y += temp_y
        s.add((x, y))
    else:
        robo_x += temp_x
        robo_y += temp_y
        s.add((robo_x, robo_y))

    mode ^= 1

print(len(s))



# PART ONE
# import sys

# with open(sys.argv[1], "r") as f:
#     content = f.read()

# x, y = 0, 0
# s = set([(x, y)])

# for c in content:
#     match c:
#         case '<':
#             x -= 1
#         case '>':
#             x += 1
#         case '^':
#             y -= 1
#         case 'v':
#             y += 1
    
#     s.add((x, y))

# print(len(s))