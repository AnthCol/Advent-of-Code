# PART TWO
import sys
from collections import defaultdict

# this sucks
def generate_combos(ingredient_count, depth, combo, combos):
    if depth == ingredient_count:
        if sum(combo) == 100:
            combos.append(combo)
        return

    for i in range(101):
        copy = combo.copy()
        copy.append(i)
        generate_combos(ingredient_count, depth + 1, copy, combos)    


def calc_score(combo, ingredients):
    stats = defaultdict(int)
    calories = 0
    for i in range(len(combo)):
        amount_of_ingredient = combo[i]
        stats['capacity']   += amount_of_ingredient * ingredients[i]['capacity']
        stats['durability'] += amount_of_ingredient * ingredients[i]['durability']
        stats['flavor']     += amount_of_ingredient * ingredients[i]['flavor']
        stats['texture']    += amount_of_ingredient * ingredients[i]['texture']     
        calories            += amount_of_ingredient * ingredients[i]['calories']

    product = 1
    for attribute in stats:
        product *= max(0, stats[attribute])
    return product if calories == 500 else 0


ingredients = []
with open(sys.argv[1], "r") as f:
    for line in f:
        parts = line.strip().split()
        stats = {
            'capacity'   : int(parts[2][:-1]),
            'durability' : int(parts[4][:-1]),
            'flavor'     : int(parts[6][:-1]),
            'texture'    : int(parts[8][:-1]),
            'calories'   : int(parts[10]),
        }
        ingredients.append(stats)

combos = []
generate_combos(len(ingredients), 0, [], combos)

highest_score = 0
for combo in combos:
    highest_score = max(highest_score, calc_score(combo, ingredients))
print(highest_score)

# PART ONE
# import sys
# from collections import defaultdict

# # this sucks
# def generate_combos(ingredient_count, depth, combo, combos):
#     if depth == ingredient_count:
#         if sum(combo) == 100:
#             combos.append(combo)
#         return

#     for i in range(101):
#         copy = combo.copy()
#         copy.append(i)
#         generate_combos(ingredient_count, depth + 1, copy, combos)    


# def calc_score(combo, ingredients):
#     stats = defaultdict(int)
#     for i in range(len(combo)):
#         amount_of_ingredient = combo[i]
#         stats['capacity']   += amount_of_ingredient * ingredients[i]['capacity']
#         stats['durability'] += amount_of_ingredient * ingredients[i]['durability']
#         stats['flavor']     += amount_of_ingredient * ingredients[i]['flavor']
#         stats['texture']    += amount_of_ingredient * ingredients[i]['texture']     

#     product = 1
#     for attribute in stats:
#         product *= max(0, stats[attribute])
#     return product


# ingredients = []
# with open(sys.argv[1], "r") as f:
#     for line in f:
#         parts = line.strip().split()
#         stats = {
#             'capacity'   : int(parts[2][:-1]),
#             'durability' : int(parts[4][:-1]),
#             'flavor'     : int(parts[6][:-1]),
#             'texture'    : int(parts[8][:-1]),
#             'calories'   : int(parts[10]),
#         }
#         ingredients.append(stats)

# combos = []
# generate_combos(len(ingredients), 0, [], combos)

# highest_score = 0
# for combo in combos:
#     highest_score = max(highest_score, calc_score(combo, ingredients))
# print(highest_score)