# PART TWO
import sys

grid = []
visited = '#'

def bad_index(grid, r, c):
    return r < 0 or r == len(grid) or c < 0 or c == len(grid[r])

def dfs(grid, r, c, shape_indices, letter):
    if bad_index(grid, r, c):
        return

    if grid[r][c] != letter:
        return

    shape_indices.add((r, c))
    grid[r][c] = visited

    dfs(grid, r, c + 1, shape_indices, letter)
    dfs(grid, r, c - 1, shape_indices, letter)
    dfs(grid, r + 1, c, shape_indices, letter)
    dfs(grid, r - 1, c, shape_indices, letter)

def check_missing(r, c, shape_indices):
    missing = 0
    # ! == r, c

    #  X?
    #  !X 
    in1 = (r, c + 1)
    in2 = (r - 1, c)
    out = (r - 1, c + 1)

    if in1 in shape_indices and in2 in shape_indices and out not in shape_indices:
        missing += 1

    # X!
    # ?X
    in1 = (r, c - 1)
    in2 = (r + 1, c)
    out = (r + 1, c - 1)

    if in1 in shape_indices and in2 in shape_indices and out not in shape_indices:
        missing += 1

    # ?X
    # X!

    in1 = (r, c - 1)
    in2 = (r - 1, c)
    out = (r - 1, c - 1)

    if in1 in shape_indices and in2 in shape_indices and out not in shape_indices:
        missing += 1


    # !X
    # X?

    in1 = (r, c + 1)
    in2 = (r + 1, c)
    out = (r + 1, c + 1)

    if in1 in shape_indices and in2 in shape_indices and out not in shape_indices:
        missing += 1


    return missing

def check_lonely(r, c, shape_indices):
    lonely = 0
    # X == r, c 

    # ??
    # ?X
    not_in_shape = (
        (r - 1, c),
        (r - 1, c - 1), 
        (r, c - 1),
    )

    if sum(1 for index in not_in_shape if index in shape_indices) == 0:
        lonely += 1

    # ?X
    # ??
    not_in_shape = (
        (r, c - 1),
        (r + 1, c),
        (r + 1, c - 1),
    )

    if sum(1 for index in not_in_shape if index in shape_indices) == 0:
        lonely += 1

    # X?
    # ??
    not_in_shape = (
        (r, c + 1), 
        (r + 1, c),
        (r + 1, c + 1),
    )

    if sum(1 for index in not_in_shape if index in shape_indices) == 0:
        lonely += 1

    # ??
    # X?
    not_in_shape = (
        (r - 1, c),
        (r - 1, c + 1), 
        (r, c + 1),
    )
    if sum(1 for index in not_in_shape if index in shape_indices) == 0:
        lonely += 1

    return lonely

def check_diamond(r, c, shape_indices, diamond_pairs):
    # ! == r, c

    # X?
    # ?!
    in1 = (r - 1, c - 1)
    out1 = (r - 1, c)
    out2 = (r, c - 1)

    if in1 in shape_indices and out1 not in shape_indices and out2 not in shape_indices:
        pair = [in1, (r, c)]
        pair.sort()
        diamond_pairs.append(tuple(pair))

    # !?
    # ?X
    in1 = (r + 1, c + 1)
    out1 = (r + 1, c)
    out2 = (r, c + 1)

    if in1 in shape_indices and out1 not in shape_indices and out2 not in shape_indices:
        pair = [in1, (r, c)]
        pair.sort()
        diamond_pairs.append(tuple(pair))

    # ?!
    # X?
    in1 = (r + 1, c - 1)
    out1 = (r + 1, c)
    out2 = (r, c - 1)

    if in1 in shape_indices and out1 not in shape_indices and out2 not in shape_indices:
        pair = [in1, (r, c)]
        pair.sort()
        diamond_pairs.append(tuple(pair))

    # ?X
    # !?
    in1 = (r - 1, c + 1)
    out1 = (r, c + 1)
    out2 = (r - 1, c)

    if in1 in shape_indices and out1 not in shape_indices and out2 not in shape_indices:
        pair = [in1, (r, c)]
        pair.sort()
        diamond_pairs.append(tuple(pair))


# Number of sides == number of corners, so determine the number of corners. 
def calc_score(shape_indices):
    if len(shape_indices) == 1:
        return 4
 
    corners = 0
    diamond_pairs = []

    for row, col in shape_indices:
        corners += check_missing(row, col, shape_indices)
        corners += check_lonely(row, col, shape_indices)
        check_diamond(row, col, shape_indices, diamond_pairs)

    sides = corners + len(diamond_pairs)
    return sides * len(shape_indices)


if __name__ == '__main__':
    with open(sys.argv[1], "r") as f:
        for line in f:
            grid.append([c for c in line.strip()])

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != visited:
                shape = set()
                letter = grid[i][j]
                dfs(grid, i, j, shape, grid[i][j])
                total += calc_score(shape)

    print(total)


# PART ONE
# import sys

# grid = []
# visited = '#'

# def bad_index(grid, r, c):
#     return r < 0 or r == len(grid) or c < 0 or c == len(grid[r])


# def dfs(grid, r, c, shape_indices, letter):
#     if bad_index(grid, r, c):
#         return

#     if grid[r][c] != letter:
#         return

#     shape_indices.add((r, c))
#     grid[r][c] = visited

#     dfs(grid, r, c + 1, shape_indices, letter)
#     dfs(grid, r, c - 1, shape_indices, letter)
#     dfs(grid, r + 1, c, shape_indices, letter)
#     dfs(grid, r - 1, c, shape_indices, letter)

# # Start by assuming all four sides, then remove as you go 
# def calc_score(shape_indices):
#     perimiter = 0
#     for row, col in shape_indices:
#         directions = (
#             (row, col + 1),
#             (row, col - 1),
#             (row + 1, col),
#             (row - 1, col),
#         )
#         neighbour_count = sum(1 for d in directions if d in shape_indices)
#         perimiter += 4 - neighbour_count

#     return perimiter * len(shape_indices)



# if __name__ == '__main__':
#     with open(sys.argv[1], "r") as f:
#         for line in f:
#             grid.append([c for c in line.strip()])

#     total = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j] != visited:
#                 shape = set()
#                 dfs(grid, i, j, shape, grid[i][j])
#                 total += calc_score(shape)

#     print(total)
