# PART TWO
import sys

def new_password(password):
    password = list(password)
    
    wrapped = True
    index = len(password) - 1
    while wrapped:
        if password[index] == 'z':
            password[index] = 'a'
            index -= 1
        else:
            password[index] = chr(ord(password[index]) + 1)
            wrapped = False

    return ''.join(password)

def check(password):
    conditions = [False] * 3

    # First condition
    triplets = [password[i : i + 3] for i in range(len(password) - 2)] 
    for part in triplets:
        if ord(part[2]) - ord(part[1]) == 1 and ord(part[1]) - ord(part[0]) == 1:
            conditions[0] = True
            break

    # Second condition
    conditions[1] = not any(char in password for char in ['i', 'o', 'l'])

    # Third condition
    twins = [password[i : i + 2] for i in range(len(password) - 1)] 
    twindata = []
    for i in range(len(twins)):
        if twins[i][0] == twins[i][1]:
            twindata.append((twins[i], i))

    for i in range(len(twindata) - 1):
        if abs(twindata[i][1] - twindata[i + 1][1]) > 1:
            conditions[2] = True
            break

    return False not in conditions

with open(sys.argv[1], "r") as f:
    password = f.read().strip()

valid = False
count = 0
while not valid:
    valid = check(password)
    if valid and count == 0:
        valid = False
        count = 1

    if not valid:
        password = new_password(password)

print(password) 

# PART ONE
# import sys

# def new_password(password):
#     password = list(password)
    
#     wrapped = True
#     index = len(password) - 1
#     while wrapped:
#         if password[index] == 'z':
#             password[index] = 'a'
#             index -= 1
#         else:
#             password[index] = chr(ord(password[index]) + 1)
#             wrapped = False

#     return ''.join(password)

# def modify(password):
#     conditions = [False] * 3

#     # First condition
#     triplets = [password[i : i + 3] for i in range(len(password) - 2)] 
#     for part in triplets:
#         if ord(part[2]) - ord(part[1]) == 1 and ord(part[1]) - ord(part[0]) == 1:
#             conditions[0] = True
#             break

#     # Second condition
#     conditions[1] = not any(char in password for char in ['i', 'o', 'l'])

#     # Third condition
#     twins = [password[i : i + 2] for i in range(len(password) - 1)] 
#     twindata = []
#     for i in range(len(twins)):
#         if twins[i][0] == twins[i][1]:
#             twindata.append((twins[i], i))

#     for i in range(len(twindata) - 1):
#         if abs(twindata[i][1] - twindata[i + 1][1]) > 1:
#             conditions[2] = True
#             break

#     valid = False not in conditions

#     if not valid:
#         password = new_password(password)

#     return valid, password

# with open(sys.argv[1], "r") as f:
#     password = f.read().strip()

# valid = False
# while not valid:
#     valid, password = modify(password)

# print(password) 
