# PART TWO
import sys
import hashlib

with open(sys.argv[1], "r") as f:
    secret_key = f.read()

val = 0
while True:
    result = hashlib.md5((secret_key + str(val)).encode())
    result = result.hexdigest()
    if result.startswith("000000"):
        print(val)
        break
    val += 1



# PART ONE
# import sys
# import hashlib

# with open(sys.argv[1], "r") as f:
#     secret_key = f.read()

# val = 0
# while True:
#     result = hashlib.md5((secret_key + str(val)).encode())
#     result = result.hexdigest()
#     if result.startswith("00000"):
#         print(val)
#         break
#     val += 1