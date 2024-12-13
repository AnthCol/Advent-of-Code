# PART TWO
import sys
import re
from copy import deepcopy

class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Prize:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Machine:
    def __init__(self, a, b, prize):
        self.A = a
        self.B = b
        self.prize = prize

with open(sys.argv[1], "r") as f:
    content = f.read().strip()
    numbers = list(map(int, re.findall(r'\d+', content)))

machines = []
for n in range(0, len(numbers), 6):
    A = Button(numbers[n], numbers[n + 1])
    B = Button(numbers[n + 2], numbers[n + 3])
    prize = Prize(numbers[n + 4], numbers[n + 5])
    prize.x += 10000000000000 
    prize.y += 10000000000000 
    machines.append(Machine(A, B, prize))

cost_a = 3
tokens_used = 0

for m in machines:
    """
    Solve equations
    94A + 22B = 8400 (X)
    34A + 67B = 5400 (Y)
    """
    original = deepcopy(m)

    m.A.x *= m.B.y
    m.B.x *= m.B.y 
    m.prize.x *= m.B.y

    m.A.y *= original.B.x
    m.B.y *= original.B.x
    m.prize.y *= original.B.x

    # We cancel out the b's
    a = m.A.x - m.A.y
    prize = m.prize.x - m.prize.y 

    a_presses = prize / a
    b_presses = (original.prize.x - (original.A.x * a_presses)) / original.B.x


    if a_presses >= 0 and b_presses >= 0:
        if a_presses == int(a_presses) and b_presses == int(b_presses):
            tokens_used += (int(a_presses) * 3) + int(b_presses)

print(tokens_used)



# PART ONE
# import sys
# import re

# class Button:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Prize:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# class Machine:
#     def __init__(self, a, b, prize):
#         self.A = a
#         self.B = b
#         self.prize = prize

# with open(sys.argv[1], "r") as f:
#     content = f.read().strip()
#     numbers = list(map(int, re.findall(r'\d+', content)))

# machines = []
# for n in range(0, len(numbers), 6):
#     A = Button(numbers[n], numbers[n + 1])
#     B = Button(numbers[n + 2], numbers[n + 3])
#     prize = Prize(numbers[n + 4], numbers[n + 5])
#     machines.append(Machine(A, B, prize))

# cost_a = 3
# tokens_used = 0

# for m in machines:
#     minimum = sys.maxsize

#     for a_presses in range(101):
#         for b_presses in range(101):
#             x = (m.A.x * a_presses) + (m.B.x * b_presses)
#             y = (m.A.y * a_presses) + (m.B.y * b_presses)

#             if x == m.prize.x and y == m.prize.y:
#                 cost = (a_presses * cost_a) + b_presses
#                 minimum = min(minimum, cost)


#     if minimum != sys.maxsize:
#         tokens_used += minimum

# print(tokens_used)