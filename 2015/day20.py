# PART TWO
import sys
import math

with open(sys.argv[1], "r") as f:
    for line in f:
        target = int(line.strip())

presents_per_elf = 11
max_visits_per_elf = 50
house_number = 1
while True:
    presents = 0
    factors = set()

    for i in range(1, int(math.sqrt(house_number)) + 1):
        if house_number % i == 0:
            factors.add(i)
            if house_number / i != i:
                factors.add(house_number // i)
                
    for factor in factors:
        if house_number / factor <= 50:
            presents += presents_per_elf * factor

    if presents >= target:
        print(house_number)
        break

    house_number += 1



# PART ONE
# import sys
# import math

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         target = int(line.strip())

# presents_per_elf = 10

# house_number = 1
# while True:
#     presents = 0
#     for i in range(1, int(math.sqrt(house_number)) + 1):
#         if house_number % i == 0:
#             presents += presents_per_elf * i
#             if house_number // i != i:
#                 presents += presents_per_elf * (house_number // i)

#     if presents >= target:
#         print(house_number)
#         break

#     house_number += 1
