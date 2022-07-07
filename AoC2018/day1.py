import sys

# Problem:   https://adventofcode.com/2018/day/1

filename = "input1.txt"

with open(filename) as file:
    data = file.readlines()

# split_data = [int(row[1:]) if row[0] == "+" else int(row) for row in data]

# print(sum(split_data))    <--answer 1

split_data = [int(row[1:]) if row[0] == "+" else int(row) for row in data]


freq_dict = {}
counter = 0
flag = True

while True and flag:

    for row in split_data:
        counter += row
        print(counter)
        if freq_dict.get(counter):
            flag = False
            print(counter)
            break
        else:
            freq_dict[counter] = 1
