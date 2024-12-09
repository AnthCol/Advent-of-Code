# PART TWO
import sys
from collections import defaultdict
from itertools import combinations

def bad_index(grid, r, c) -> bool:
    return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r])


def count_antinodes(grid, node_locations, antinode_locations) -> None:
    combos = list(combinations(node_locations, 2))
    for c in combos:
        point1 = c[0]
        point2 = c[1]
        rowdif = point1[0] - point2[0]
        coldif = point1[1] - point2[1]

        arowdif = abs(rowdif)
        acoldif = abs(coldif)

        new_points = []

        # this is innefficient and bad but I cba. 
        # 'extend' the grid and include a bunch of points 
        # outside the grid and filter them after because 
        # I don't feel like writing something good at the moment
        # 
        # It's so bad lol
        # Could prob make a nice recursive function to do this instead
        loops = len(grid)
        rp1, cp1, rp2, cp2 = point1[0], point1[1], point2[0], point2[1]

        # Only one of the following will be true
        if rowdif < 0 and coldif < 0:
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                rp1 -= arowdif
                cp1 -= acoldif
                rp2 += arowdif
                cp2 += acoldif

        elif rowdif < 0  and coldif == 0:
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                rp1 -= arowdif
                rp2 += arowdif

        elif rowdif < 0 and coldif > 0:
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                rp1 -= arowdif
                cp1 += acoldif
                rp2 += arowdif
                cp2 -= acoldif

        elif rowdif == 0  and coldif < 0:  
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                cp1 -= acoldif
                cp2 += acoldif

        elif rowdif == 0 and coldif > 0: 
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                cp1 += acoldif 
                cp2 -= acoldif

        elif rowdif > 0 and coldif < 0: 
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                rp1 += arowdif
                cp1 -= acoldif
                rp2 -= arowdif
                cp2 += acoldif

        elif rowdif > 0 and coldif == 0: 
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                rp1 += arowdif
                rp2 -= arowdif

        elif rowdif > 0 and coldif > 0:
            for _ in range(loops):
                new_points.append((rp1, cp1))
                new_points.append((rp2, cp2))
                rp1 += arowdif 
                cp1 += acoldif
                rp2 -= arowdif
                cp2 -= acoldif

        for location in new_points:
            if not bad_index(grid, location[0], location[1]):
                antinode_locations.add(location)


antenna_locations = defaultdict(list)
grid = []

with open(sys.argv[1], "r") as f:
    for line in f:
        grid.append([c for c in line.strip()])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            antenna_locations[grid[i][j]].append((i, j))

antinodes = set()
for l in antenna_locations:
    count_antinodes(grid, antenna_locations[l], antinodes)
print(len(antinodes))


# PART ONE
# import sys
# from collections import defaultdict
# from itertools import combinations

# def bad_index(grid, r, c) -> bool:
#     return r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r])


# def count_antinodes(grid, node_locations, antinode_locations) -> None:
#     combos = list(combinations(node_locations, 2))
#     for c in combos:
#         point1 = c[0]
#         point2 = c[1]
#         rowdif = point1[0] - point2[0]
#         coldif = point1[1] - point2[1]

#         arowdif = abs(rowdif)
#         acoldif = abs(coldif)

#         new_points = []

#         # Only one of the following will be true
#         if rowdif < 0 and coldif < 0:
#             new_points.append([point1[0] - arowdif, point1[1] - acoldif])
#             new_points.append([point2[0] + arowdif, point2[1] + acoldif])

#         elif rowdif < 0  and coldif == 0:
#             new_points.append([point1[0] - arowdif, point1[1]])
#             new_points.append([point2[0] + arowdif, point2[1]])

#         elif rowdif < 0 and coldif > 0:
#             new_points.append([point1[0] - arowdif, point1[1] + acoldif])
#             new_points.append([point2[0] + arowdif, point2[1] - acoldif])

#         elif rowdif == 0  and coldif < 0:  
#             new_points.append([point1[0], point1[1] - acoldif])
#             new_points.append([point2[0], point2[1] + acoldif])

#         elif rowdif == 0 and coldif > 0: 
#             new_points.append([point1[0], point1[1] + acoldif])
#             new_points.append([point2[0], point2[1] - acoldif])

#         elif rowdif > 0 and coldif < 0: 
#             new_points.append([point1[0] + arowdif, point1[1] - acoldif])
#             new_points.append([point2[0] - arowdif, point2[1] + acoldif])

#         elif rowdif > 0 and coldif == 0: 
#             new_points.append([point1[0] + arowdif, point1[1]])
#             new_points.append([point2[0] - arowdif, point2[1]])

#         elif rowdif > 0 and coldif > 0:
#             new_points.append([point1[0] + arowdif, point1[1] + acoldif])
#             new_points.append([point2[0] - arowdif, point2[1] - acoldif])

#         """
#         If rowdif is positive and coldif is negative:
#         ..s
#         ...
#         f..

#         If rowdif is positive and coldif is zero:
#         .s.
#         ...
#         .f.


#         If rowdif is positive and coldif is positive:

#         s..
#         ...
#         ..f
        
#         -----

#         If rowdif is negative and coldif is negative:
#         f..
#         ...
#         ..s

#         If rowdif is negative and coldif is zero:
#         .f.
#         ...
#         .s.

#         If rowdif is negative and coldif is positive:
#         ..f
#         ...
#         s..

#         If rowdif is zero and coldif is negative:
#         ...
#         f.s
#         ...

#         If rowdif is zero and coldif is positive:
#         ...
#         s.f
#         ... 
    
#         If rowdif is positive and coldif is negative:
        
#         If rowdif is positive and coldif is zero:

#         If rowdif is positiv and coldif is positive:

#         """ 

#         for location in new_points:
#             if not bad_index(grid, location[0], location[1]):
#                 antinode_locations.add(tuple(location))


# antenna_locations = defaultdict(list)
# grid = []

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         grid.append([c for c in line.strip()])

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] != '.':
#             antenna_locations[grid[i][j]].append((i, j))

# antinodes = set()
# for l in antenna_locations:
#     count_antinodes(grid, antenna_locations[l], antinodes)
# print(len(antinodes))
