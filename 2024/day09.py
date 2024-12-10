# PART TWO
import sys

with open(sys.argv[1], "r") as f:
    diskmap = f.read().strip()

file_id = 0
curr = 0
disk = []
files = []
spaces = []

for i in range(len(diskmap)):
    number = int(diskmap[i])

    if number == 0:
        continue 
    
    if i % 2 == 0:
        disk.extend([file_id] * number)
        files.append((file_id, [curr + j for j in range(number)]))
        file_id += 1
    else:
        disk.extend([-1] * number)
        spaces.append([curr + j for j in range(number)])

    curr += number

replaced = True
while replaced:
    d = disk.copy()

    replaced = False

    last_file = files[-1]
    file_id = last_file[0]
    file_len = len(last_file[1]) 
    file_indices = last_file[1]
    file_as_string = str(file_id) * file_len

    space_indices = spaces[0]     
    space_len = len(spaces[0])

    if file_len == space_len:
        for i in space_indices:
            d[i] = file_id
        del spaces[0]
        replaced = True
        disk = d

    elif file_len < space_len:
        amount_consumed = 0
        while amount_consumed < file_len:
            
            amount_consumed += 1


    # If no replacement, there was not a place for that file. 

        for i in space_indices:
            if i < file_len:


    


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
