# PART TWO
import sys


def get_next_position(grid, position):
    direction, row, col = position

    next_position = {
        'north' : (row - 1, col),
        'east'  : (row, col + 1),
        'south' : (row + 1, col),
        'west'  : (row, col - 1),
    }

    nrow, ncol = next_position[direction]

    if bad_index(grid, nrow, ncol):
        return (direction, nrow, ncol)

    if grid[nrow][ncol] == '.':
        return (direction, nrow, ncol)
        
    newdir = {
        'north' : 'east',
        'east'  : 'south',
        'south' : 'west',
        'west'  : 'north',
    }

    while grid[nrow][ncol] == '#':
        direction = newdir[direction]
        nrow, ncol = next_position[direction]

    return (direction, nrow, ncol)

def bad_index(grid, r, c):
    return r < 0 or r >= len(grid) or c < 0 or c >= (len(grid[r]))

def cycle(grid, position):
    visited = set()

    while position not in visited:
        visited.add(position)
        position = get_next_position(grid, position) 
        if bad_index(grid, position[1], position[2]):
            return False 

    return True
 
grid = []

row_count = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        row = []
        for i in range(len(line.strip())):
            if line[i] == '^':
                starting = ('north', row_count, i)
            row.append(line[i]) 
        grid.append(row)
        row_count += 1

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '^' and grid[i][j] != '#':
            grid[i][j] = '#' 
            if cycle(grid, starting):
                count += 1 
            grid[i][j] = '.'

print(count)


# PART ONE
# import sys

# def bad_index(grid, r, c):
#     return r < 0 or r >= len(grid) or c < 0 or c >= (len(grid[r]))

# count = 0

# def dfs(grid, position, direction, visited):
#     visited.add(position)

#     row = position[0]
#     col = position[1]

#     next_position = {
#         'north' : (row - 1, col),
#         'east'  : (row, col + 1),
#         'south' : (row + 1, col),
#         'west'  : (row, col - 1),
#     }

#     newdir = {
#         'north' : 'east',
#         'east'  : 'south',
#         'south' : 'west',
#         'west'  : 'north',
#     }


#     nrow, ncol = next_position[direction]

#     # officer left
#     if bad_index(grid, nrow, ncol):
#         return  

#     while grid[nrow][ncol] == '#':
#         direction = newdir[direction]
#         nrow, ncol = next_position[direction]

#     dfs(grid, (nrow, ncol), direction, visited)

# # bruh
# sys.setrecursionlimit(10000)
    
# grid = []
# visited = set()

# row_count = 0
# with open(sys.argv[1], "r") as f:
#     for line in f:
#         row = []
#         for i in range(len(line.strip())):
#             if line[i] == '^':
#                 visited.add((row_count, i))
#             row.append(line[i]) 
#         grid.append(row)
#         row_count += 1

# direction = 'north'
# position = list(visited)[0]
# dfs(grid, position, direction, visited)

# print(len(visited))
