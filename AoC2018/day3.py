import numpy as np

with open("input3.txt") as file:
    data = [line.strip() for line in file.readlines()]

lines = [row.split()[2:] for row in data]

fabric = np.zeros((1000, 1000))

for line in lines:

    # first part of input, top left corner of segment
    x, y = [int(j) for j in line[0].strip(":").split(",")]

    # second part of input, width/height of segment
    rows, cols = [int(k) for k in line[1].split("x")]

    # increment 1 for each element of the array to keep track of overlaps
    fabric[x : x + rows, y : y + cols] = (fabric[x : x + rows, y : y + cols] + 1).copy()

# part 1 solution
(fabric > 1).sum()


# part 2 solution
for i, line in enumerate(lines):

    x, y = [int(j) for j in line[0].strip(":").split(",")]
    rows, cols = [int(k) for k in line[1].split("x")]

    if (fabric[x : x + rows, y : y + cols] == 1).sum() == rows * cols:
        print(i + 1)
