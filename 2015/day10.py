# PART TWO
import sys
import re

with open(sys.argv[1], "r") as f:
    content = f.read().strip()

for i in range(50):
    modified = ""
    repeating_parts = [match.group(0) for match in re.compile(r'(.)\1*').finditer(content)]
    modified = ''.join(str(len(part)) + part[0] for part in repeating_parts) 
    content = modified

print(len(modified))


# # PART ONE
# import sys
# import re

# with open(sys.argv[1], "r") as f:
#     content = f.read().strip()

# for i in range(40):
#     modified = ""
#     repeating_parts = [match.group(0) for match in re.compile(r'(.)\1*').finditer(content)]
#     for part in repeating_parts:
#         modified += str(len(part)) + part[0]
#     content = modified

# print(len(modified))
