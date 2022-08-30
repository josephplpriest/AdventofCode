# coding: utf-8
from collections import Counter


with open("input8.txt") as file:
    data = file.read().split("\n")

data = [row.split(" | ") for row in data[:-1]]

print()


for row in data[0:5]:

    num_dict = {}
    

    num_set = [set(string) for string in row[0].split()]

    
    for s in num_set:
        if len(s) == 2:
            num_dict[1] = s
        elif len(s) == 3:
            num_dict[7] = s
        elif len(s) == 7:
            num_dict[8] = s
        elif len(s) == 4:
            num_dict[4] = s
        else:
            pass
    
    other_nums = [num for num in num_set if len(num) not in [2,3,4,7]]

    for o_n in other_nums:
        if len(o_n - num_dict[1]) == 3:
            num_dict[3] = o_n

    
