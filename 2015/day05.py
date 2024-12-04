# PART TWO
import sys

def isvowel(char):
    return char in ['a', 'e', 'i', 'o', 'u']

def isbad(substring):
    return substring in ['ab', 'cd', 'pq', 'xy']

nice = 0 

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()

        twos = [line[i : i + 2] for i in range(len(line))]
        threes = [line[i : i + 3] for i in range(len(line))]

        two_check = False
        three_check = False

        for i in range(len(twos)):
            for j in range(len(twos)):
                # cannot be next to eachother
                if i == j or abs(i - j) == 1:
                    continue
                
                if twos[i] == twos[j]:
                    two_check = True
                    break

        for s in threes:
            if len(s) == 3 and s[0] == s[2]:
                three_check = True
                break
        
        if two_check and three_check:
            nice += 1

print(nice)

# PART ONE
# import sys

# def isvowel(char):
#     return char in ['a', 'e', 'i', 'o', 'u']

# def isbad(substring):
#     return substring in ['ab', 'cd', 'pq', 'xy']

# nice = 0 

# with open(sys.argv[1], "r") as f:
#     for line in f:
#         vowels = 0
#         contains_bad = False
#         contains_double = False

#         prev = '\0'

#         for i in range(len(line)):
#             if isbad(line[i : i + 2]):
#                 contains_bad = True
#                 break
            
#             if isvowel(line[i]):
#                 vowels += 1

#             if prev == line[i]:
#                 contains_double = True
#             prev = line[i]

#         if contains_double and vowels >= 3 and not contains_bad:
#             nice += 1

# print(nice)