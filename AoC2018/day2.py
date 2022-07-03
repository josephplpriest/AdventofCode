from collections import Counter

filename = "input2.txt"

with open(filename) as file:
    data = [line.strip() for line in file.readlines()]

#Part 1

#for each input, check if it contains doubles or triplets of the same character
#increment counter variables for each then multiply for the answer

# counts = [Counter(row) for row in data]

# doubles = 0
# triples = 0

# for count in counts:
#     if 2 in count.values():
#         doubles += 1
#     if 3 in count.values():
#         triples += 1

# print(doubles * triples)

