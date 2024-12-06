# PART TWO
import sys
from collections import defaultdict

reindeer = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        tokens = line.strip().split()
        reindeer[(int(tokens[3]), int(tokens[6]), int(tokens[13]))] = 0

max_time = 2503
max_dist = 0

stats = defaultdict(lambda: [0] * max_time)
reindeer_id = 0
for speed, running_time, resting_time in reindeer:
    dist = 0
    mode = 0
    timer = 0
    while timer < max_time:
        if mode == 0:
            for sec in range(running_time):
                stats[reindeer_id][timer] = dist
                dist += speed
                timer += 1
                if timer == max_time:
                    break
        else:
            for sec in range(resting_time):
                stats[reindeer_id][timer] = dist
                timer += 1
                if timer == max_time:
                    break
        mode ^= 1
    max_dist = max(max_dist, dist)
    reindeer_id += 1

scores = defaultdict(int)
max_score = 0

for time in range(max_time):
    # "at the end of each second"
    if time > 0:
        max_value = 0 
        for rein in stats:
            max_value = max(max_value, stats[rein][time])

        for rein in stats:
            if stats[rein][time] == max_value:
                scores[rein] += 1
                max_score = max(max_score, scores[rein])

print(max_score)


# # PART ONE
# import sys

# reindeer = {}

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         tokens = line.strip().split()
#         reindeer[(int(tokens[3]), int(tokens[6]), int(tokens[13]))] = 0

# max_time = 2503
# max_dist = 0
# for speed, running_time, resting_time in reindeer:
#     dist = 0
#     mode = 0
#     timer = 0
#     while timer < max_time:
#         if mode == 0:
#             for sec in range(running_time):
#                 dist += speed
#                 timer += 1
#                 if timer == max_time:
#                     break
#         else:
#             for sec in range(resting_time):
#                 timer += 1
#                 if timer == max_time:
#                     break
#         mode ^= 1
#     max_dist = max(max_dist, dist)

# print(max_dist)