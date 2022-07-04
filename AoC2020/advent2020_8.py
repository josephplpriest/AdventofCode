import numpy as np
import sys

with open("input8.txt") as file:
    data = file.read().split("\n")


visited = np.zeros(len(data)).astype(bool)


commands = [[line.split()[0], int(line.split()[1]), visit] for line, visit in zip(data, visited)]

acc = 0
row_index = 590

opp_jmp_indices = [[i, True, False] if row[0] in ["opp", "jmp"] else [i, False, False] for i, row in enumerate(commands)]

visits = []

while True:
    
    print(commands[row_index], row_index)
    if commands[row_index][2]:
        print(row_index, acc)
        break
    else:
        commands[row_index][2] = True
    command = commands[row_index][0]
    distance = commands[row_index][1]
    if command == "nop":
        row_index += 1
        visits.append(row_index)
    elif command == "acc":
        acc += distance
        row_index += 1
    else:
        #jump
        row_index += distance
        visits.append(row_index)


