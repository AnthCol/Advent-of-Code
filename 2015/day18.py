# PART TWO
import sys
from copy import deepcopy

def bad_index(grid, r, c):
    return r < 0 or r == len(grid) or c < 0 or c == (len(grid[r]))

def corner(grid, r, c):
    corners = (
        r == 0 and c == 0,
        r == 0 and c == len(grid[0]) - 1,
        r == len(grid) - 1 and c == 0,
        r == len(grid) - 1 and c == len(grid[0]) - 1,
    )
    return True in corners

def determine(grid, r, c):

    positions = [
        (r + 1, c),
        (r + 1, c + 1), 
        (r + 1, c - 1),
        (r, c + 1),
        (r, c - 1), 
        (r - 1, c),
        (r - 1, c + 1),
        (r - 1, c - 1),
    ]

    on_count = 0
    for pair in positions:
        if not bad_index(grid, pair[0], pair[1]) and grid[pair[0]][pair[1]] == '#':
            on_count += 1

    nextchar = '.'
    current_status = 'on' if grid[r][c] == '#' else 'off'

    if current_status == 'on' and on_count in [2, 3]:
        nextchar = '#'
    elif current_status == 'off' and on_count == 3:
        nextchar = '#'

    return nextchar


def modify_grid(grid):
    nextgrid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not corner(grid, i, j):
                nextgrid[i][j] = determine(grid, i, j) 
    return nextgrid

neighbour_grid = []
with open(sys.argv[1], "r") as f:
    for line in f:
        neighbour_grid.append([c for c in line.strip()])

corners = (
    (0, 0),
    (0, len(neighbour_grid[0]) - 1),
    (len(neighbour_grid) - 1, 0),
    (len(neighbour_grid) - 1, len(neighbour_grid[0]) - 1),
)

for r, c in corners:
    neighbour_grid[r][c] = '#'

for _ in range(100):
    neighbour_grid = modify_grid(neighbour_grid)

print(sum(1 for row in neighbour_grid for light in row if light == '#'))


# PART ONE
# import sys
# from copy import deepcopy

# def bad_index(grid, r, c):
#     return r < 0 or r == len(grid) or c < 0 or c == (len(grid[r]))

# def determine(grid, r, c):

#     positions = [
#         (r + 1, c),
#         (r + 1, c + 1), 
#         (r + 1, c - 1),
#         (r, c + 1),
#         (r, c - 1), 
#         (r - 1, c),
#         (r - 1, c + 1),
#         (r - 1, c - 1),
#     ]

#     on_count = 0
#     for pair in positions:
#         if not bad_index(grid, pair[0], pair[1]) and grid[pair[0]][pair[1]] == '#':
#             on_count += 1

#     nextchar = '.'
#     current_status = 'on' if grid[r][c] == '#' else 'off'

#     if current_status == 'on' and on_count in [2, 3]:
#         nextchar = '#'
#     elif current_status == 'off' and on_count == 3:
#         nextchar = '#'

#     return nextchar


# def modify_grid(grid):
#     nextgrid = deepcopy(grid)
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             nextgrid[i][j] = determine(grid, i, j) 
#     return nextgrid

# neighbour_grid = []
# with open(sys.argv[1], "r") as f:
#     for line in f:
#         neighbour_grid.append([c for c in line.strip()])

# for _ in range(100):
#     neighbour_grid = modify_grid(neighbour_grid)

# print(sum(1 for row in neighbour_grid for light in row if light == '#'))