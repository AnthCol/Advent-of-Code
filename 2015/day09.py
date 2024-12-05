# PART TWO
import sys
from collections import defaultdict

longest = 0

def find_shortest(current_location, paths, distance, visited): 
    found = visited.copy()
    found.add(current_location)

    if len(paths.keys()) == len(found):
        global longest
        longest = max(longest, distance)
        return 

    for future_location, dist_from_current in paths[current_location]:
        if future_location not in visited:
            updated_distance = distance + dist_from_current
            find_shortest(future_location, paths, updated_distance, found)


paths = defaultdict(list)

with open(sys.argv[1], "r") as f:
    for line in f:
        info = line.split()
        place1, place2, distance = info[0], info[2], int(info[4])
        paths[place1].append((place2, distance))
        paths[place2].append((place1, distance))


for location in paths.keys():
    find_shortest(location, paths, 0, set()) 

print(longest)


# PART ONE
# import sys
# from collections import defaultdict

# shortest = sys.maxsize

# def find_shortest(current_location, paths, distance, visited): 
#     found = visited.copy()
#     found.add(current_location)

#     if len(paths.keys()) == len(found):
#         global shortest 
#         shortest = min(shortest, distance)
#         return 

#     for future_location, dist_from_current in paths[current_location]:
#         if future_location not in visited:
#             updated_distance = distance + dist_from_current
#             find_shortest(future_location, paths, updated_distance, found)


# paths = defaultdict(list)

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         info = line.split()
#         place1, place2, distance = info[0], info[2], int(info[4])
#         paths[place1].append((place2, distance))
#         paths[place2].append((place1, distance))


# for location in paths.keys():
#     find_shortest(location, paths, 0, set()) 

# print(shortest)
