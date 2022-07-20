import numpy as np


with open("input5.txt") as file:
    data = file.readlines()

data = [row.strip() for row in data]

coords = [instruction.split(" -> ") for instruction in data]

int_coords = []

for row in coords:
    int_coords.append(((int(x) for x in row[0].split(",")), (int(y) for y in row[1].split(","))))

ocean_floor = np.zeros((1000,1000))

for row in int_coords:
    x1, y1 = row[0]
    x2, y2 = row[1]
    
    if x1!=x2 and y1 != y2:

        if x1 > x2:
            x_indices = range(x1+1, x2, -1)
        else:
            x_indices = range(x1, x2+1)

        if y1 > y2:
            y_indices = range()

    else:
        if x1==x2:
            #horizontal line
            start, end = min(y1, y2), max(y1, y2)
            ocean_floor[x1, start:end+1] = ocean_floor[x1, start:end+1] + 1

        else:
            #vertical line
            start, end = min(x1, x2), max(x1, x2)
            ocean_floor[start:end+1, y1] = ocean_floor[start:end+1, y1] + 1

print(np.count_nonzero(ocean_floor >= 2))