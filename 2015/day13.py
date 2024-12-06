# PART ONE
import sys
from collections import defaultdict

combos = []
maxhappy = 0

def backtrack(name, people, seating):
    sat = seating.copy()
    sat.append(name)

    if len(sat) == len(people.keys()):
        global maxhappy
        maxhappy = max(maxhappy, score(people, sat))
        return

    for person, _ in people[name]:
        if person not in sat:
            backtrack(person, people, sat)

def calc(name, beside, people):
    score = 0
    for b in beside:
        for person, value in people[name]:
            if person == b:
                score += value
                break
    return score

def score(people, seating):
    score = 0

    for i in range(len(seating)):
        person = seating[i]
        if i == 0:
            beside = [seating[-1], seating[1]]
        elif i == len(seating) - 1:
            beside = [seating[i - 1], seating[0]]
        else:
            beside = [seating[i - 1], seating[i + 1]]
        
        score += calc(person, beside, people)

    return score

people = defaultdict(list)

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()[:-1].split()
        name1, name2, amount = line[0], line[-1], int(line[3])
        if line[2] == 'lose':
            amount = -amount
        people[name1].append((name2, amount))

names = list(people.keys())
for name in names:
    people[name].append(('Anthony', 0))
    people['Anthony'].append((name, 0))

for name in people.keys():
    backtrack(name, people, [])


# for combo in combos:
#     maxhappy = max(maxhappy, score(people, combo))

print(maxhappy)



# PART ONE
# import sys
# from collections import defaultdict

# combos = []

# def backtrack(name, people, seating):
#     sat = seating.copy()
#     sat.append(name)

#     if len(sat) == len(people.keys()):
#         global combos
#         combos.append(sat)
#         return

#     for person, _ in people[name]:
#         if person not in sat:
#             backtrack(person, people, sat)

# def calc(name, beside, people):
#     score = 0
#     for b in beside:
#         for person, value in people[name]:
#             if person == b:
#                 score += value
#                 break
#     return score

# def score(people, seating):
#     score = 0

#     for i in range(len(seating)):
#         person = seating[i]
#         if i == 0:
#             beside = [seating[-1], seating[1]]
#         elif i == len(seating) - 1:
#             beside = [seating[i - 1], seating[0]]
#         else:
#             beside = [seating[i - 1], seating[i + 1]]
        
#         score += calc(person, beside, people)

#     return score

# people = defaultdict(list)

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         line = line.strip()[:-1].split()
#         name1, name2, amount = line[0], line[-1], int(line[3])
#         if line[2] == 'lose':
#             amount = -amount
#         people[name1].append((name2, amount))

# for name in people.keys():
#     backtrack(name, people, [])

# maxhappy = 0

# for combo in combos:
#     maxhappy = max(maxhappy, score(people, combo))

# print(maxhappy)
