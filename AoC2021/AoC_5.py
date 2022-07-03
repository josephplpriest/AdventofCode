import numpy as np

matrix = np.zeros((1000,1000))

with open("input5.txt") as file:
    data = file.readlines()

data = [row.strip() for row in data]

coords = [instruction.split(" -> ") for instruction in data]




map(fun, coords)



