import numpy as np
import sys
import logging

filename = "input4.txt"

with open(filename) as file:
    data = file.read()

separated = data.split("\n\n")

draws, *boards = separated

draws = [int(x) for x in draws.split(",")]

remove_linebreaks = lambda x: x.replace("\n", " ")

boards = map(remove_linebreaks, boards)

convert_to_int = lambda x: [int(i) for i in x.split()]

boards = map(convert_to_int, boards)

convert_to_array = lambda x: np.reshape(x, (5,5))

boards = map(convert_to_array, boards)

boards = list(boards)

matched_nums = [np.zeros((5,5)) for i in range(100)]


drawn_nums = []

for n in draws:
    print(n)

    for i, board in enumerate(boards):
        print(matched_nums[i], board)

        matched_nums[i] += (board == n)
        
        for j in range(5):
            if (matched_nums[i][j,:].all() == True) or (matched_nums[i][:,j].all() == True):
                print("Success", n)
                
                print(sum(board[matched_nums[i]==0]) * n)
                sys.exit()
    
   