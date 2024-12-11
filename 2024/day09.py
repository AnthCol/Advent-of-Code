# PART TWO
import sys

def replace(space_locs, file_locs, disk):
    d = disk
    i = 0
    while i < len(file_locs):
        space = space_locs[i]
        file = file_locs[i]
        d[space], d[file] = d[file], d[space]
        i += 1

    unused = []
    if len(file_locs) < len(space_locs):
        unused = space_locs[i:]

    return d, unused


def update_spaces(space_locs, to_add):
    extended = False

    for i in range(len(space_locs)):
        if space_locs[i][-1] == to_add[0] - 1:
            space_locs[i].extend(to_add)
            extended = True
            break
        elif space_locs[i][0] == to_add[-1] + 1:
            space_locs[i] = to_add + space_locs[i]
            extended = True
            break

    if not extended:
        space_locs.append(to_add)


with open(sys.argv[1], "r") as f:
    diskmap = f.read().strip()

file_id = 0
curr = 0
disk = []
files = {}
spaces = []

for i in range(len(diskmap)):
    number = int(diskmap[i])

    if number == 0:
        continue 
    
    if i % 2 == 0:
        disk.extend([file_id] * number)
        files[file_id] =  [curr + j for j in range(number)]
        file_id += 1
    else:
        disk.extend([-1] * number)
        spaces.append([curr + j for j in range(number)])

    curr += number 


current_id = file_id - 1

while current_id >= 0 :
    spaces.sort()

    for i in range(len(spaces)):
        s = spaces[i]
        f = files[current_id]

        # If the space starts after the file, don't replace it
        if s[0] > f[-1]:
            continue

        if len(s) == len(f):
            disk, _ = replace(s, f, disk)
            del spaces[i]
            update_spaces(spaces, f)
            break 

        elif len(s) > len(f):
            disk, unused = replace(s, f, disk)
            del spaces[i]
            update_spaces(spaces, f)
            update_spaces(spaces, unused)
            break

    current_id -= 1


print(sum(i * value for i, value in enumerate(disk) if value > 0))


# PART ONE
# import sys

# with open(sys.argv[1], "r") as f:
#     diskmap = f.read().strip()

# file_id = 0
# disk = []
# for i in range(len(diskmap)):
#     number = int(diskmap[i])
#     # even is file
#     # odd is space
#     if i % 2 == 0:
#         disk.extend([file_id] * number)
#         file_id += 1
#     else:
#         disk.extend([-1] * number)

# number_locations = []
# blank_locations = []
# for i, value in enumerate(disk):
#     if value != -1:
#         number_locations.append(i)
#     else:
#         blank_locations.append(i)


# j = len(number_locations) - 1
# for i in range(len(blank_locations)):
#     blank_loc = blank_locations[i]
#     num_loc = number_locations[j]

#     if num_loc < blank_loc:
#         break

#     disk[num_loc], disk[blank_loc] = disk[blank_loc], disk[num_loc]
#     j -= 1


# print(sum(i * value for i, value in enumerate(disk) if value > 0))
