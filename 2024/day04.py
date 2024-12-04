# PART TWO
import sys

grid = []

def bad_index(row, col):
    return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row])

def traverse(grid, row, col):
    indices = {
        'nw' : (row - 1, col - 1),
        'ne' : (row - 1, col + 1),
        'sw' : (row + 1, col - 1),
        'se' : (row + 1, col + 1),
    }

    if grid[row][col] != 'A':
        return False

    letters = {}

    for direction in indices:
        r = indices[direction][0]
        c = indices[direction][1]
        if bad_index(r, c):
            return False
        letters[direction] = grid[r][c]
        
    combos = (
        letters['nw'] == 'M' and letters['se'] == 'S',
        letters['ne'] == 'M' and letters['sw'] == 'S',
        letters['se'] == 'M' and letters['nw'] == 'S',
        letters['sw'] == 'M' and letters['ne'] == 'S',
    )

    return sum(1 for combo in combos if combo) == 2

with open(sys.argv[1], "r") as f:
    for line in f:
        grid.append([char for char in line.strip()])

count = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if traverse(grid, row, col):
            count += 1

            
print(count)


# # PART ONE
# import sys

# grid = []
# targets = ['X', 'M', 'A', 'S'] 

# def bad_index(grid, row, col):
#     return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row])

# def traverse(grid, row, col, target_index, mode):
#     modes = {
#         'forwards'      : (row, col + 1),
#         'backwards'     : (row, col - 1),
#         'ne diag'       : (row - 1, col + 1),
#         'nw diag'       : (row - 1, col - 1),
#         'se diag'       : (row + 1, col + 1),
#         'sw diag'       : (row + 1, col - 1),
#         'down'          : (row + 1, col),
#         'up'            : (row - 1, col),
#     }

#     if target_index == len(targets):
#         return True

#     if bad_index(grid, row, col):
#         return False

#     if grid[row][col] != targets[target_index]:
#         return False

#     row = modes[mode][0]
#     col = modes[mode][1]
    
#     return traverse(grid, row, col, target_index + 1, mode)


# with open(sys.argv[1], "r") as f:
#     for line in f:
#         grid.append([char for char in line.strip()])

# count = 0

# for row in range(len(grid)):
#     for col in range(len(grid[row])):
#         modes = ['forwards', 'backwards', 'ne diag', 'nw diag', 'se diag', 'sw diag', 'down', 'up']
#         for mode in modes:
#             if traverse(grid, row, col, 0, mode):
#                 count += 1
            
# print(count)

