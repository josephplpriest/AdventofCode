import hashlib
import sys
# Part 1

# counter = 1
# while True:
    
#     h = hashlib.new("md5")

#     data = f"ckczppom{str(counter)}"

#     data = bytes(data, "utf-8")

#     h.update(data)

#     if str(h.hexdigest())[0:5] == "00000":
#         print(counter)
#         sys.exit()

#     counter += 1


# Part 2

counter = 1
while True:
    
    h = hashlib.new("md5")

    data = f"ckczppom{str(counter)}"

    data = bytes(data, "utf-8")

    h.update(data)

    if str(h.hexdigest())[0:6] == "000000":
        print(counter)
        sys.exit()

    counter += 1