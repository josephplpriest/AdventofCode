from operator import mul
from functools import reduce

with open("input3.txt") as file:
    data = file.readlines()

data = [row.strip() for row in data]

def get_count(x,y):
    tree_count = 0

    for i, row in enumerate(data[::y]):
        
        position = i*x

        #using modulus, get correct position regardless if extending past the end
        if row[position % len(row)] == "#":
            tree_count += 1

    return tree_count

routes_to_check = [(1,1), (3,1), (5,1), (7,1), (1,2)]

print(reduce(mul, [get_count(*route) for route in routes_to_check]))    