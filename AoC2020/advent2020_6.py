with open("input6.txt") as file:
    data = file.read()

data = data.split("\n\n")

# groups = [set(list(x.replace("\n", ''))) for x in data]

# total = 0

# for group in groups:
#     total += len(group)

# print(total)

##Part 2:

groups = [x.split("\n") for x in data]

from functools import reduce

total = 0

for group in groups:
    yeses = [set(list(g)) for g in group]

    total += len(reduce(set.intersection, yeses))


print(total)
