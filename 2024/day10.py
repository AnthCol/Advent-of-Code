# PART TWO
import sys


def bad_index(grid, r, c):
    return r < 0 or r == len(grid) or c < 0 or c == len(grid[r])

def dfs(prev, grid, locations, r, c, paths):
    if bad_index(grid, r, c):
        return

    if grid[r][c] == '.':
        return

    current = int(grid[r][c])
    if current - prev != 1:
        return

    locations.add((r, c))

    if current == 9:
        paths.add(tuple(locations.copy()))
        return

    directions = (
        (r + 1, c), 
        (r - 1, c),
        (r, c + 1),
        (r, c - 1),
    )

    for row, col in directions:
        dfs(current, grid, locations.copy(), row, col, paths)


grid = []
with open(sys.argv[1], "r") as f:
    for line in f:
        grid.append([c for c in line.strip()])

scores = 0
for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == '0':
            locs = set()
            all_paths = set()
            dfs(-1, grid, locs, i, j, all_paths)
            scores += len(all_paths)

print(scores)
        
# PART ONE
# import sys


# def bad_index(grid, r, c):
#     return r < 0 or r == len(grid) or c < 0 or c == len(grid[r])

# def dfs(prev, grid, locations, r, c):
#     if bad_index(grid, r, c):
#         return

#     if grid[r][c] == '.':
#         return

#     current = int(grid[r][c])
#     if current - prev != 1:
#         return

#     if current == 9:
#         locations.add((r, c))
#         return

#     directions = (
#         (r + 1, c), 
#         (r - 1, c),
#         (r, c + 1),
#         (r, c - 1),
#     )

#     for row, col in directions:
#         dfs(current, grid, locations, row, col)


# grid = []
# with open(sys.argv[1], "r") as f:
#     for line in f:
#         grid.append([c for c in line.strip()])

# scores = 0
# for i, row in enumerate(grid):
#     for j, char in enumerate(row):
#         if char == '0':
#             locs = set()
#             dfs(-1, grid, locs, i, j)
#             scores += len(locs)

# print(scores)
        