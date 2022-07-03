# for rounding
from math import floor

# Problem Description:
# https://adventofcode.com/2019/day/1


with open("input1.txt") as file:
    data = [int(row.strip()) for row in file.readlines()]
    

#Part 1
sum([floor(x / 3) - 2 for x in data])

from math import inf

#Part 2      
def my_fuel(n):
    if n <= 0:
        return [0]
    else: 
        return my_fuel(floor(n/3)-2) + [n]

print(sum([sum(my_fuel(row)[:-1]) for row in data]))