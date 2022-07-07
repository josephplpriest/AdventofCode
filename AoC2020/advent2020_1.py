import pandas as pd
import sys

with open("input.txt") as file:
    input_nums = file.readlines()

nums = [int(num.strip()) for num in input_nums]

odds = [n for n in nums if n // 2 != 0]

evens = [n for n in nums if n // 2 == 0]

answer = (0, 0)

used_odds = {}
used_evens = {}

for i, n1 in enumerate(odds):

    for j, n2 in enumerate(odds[i + 1 :]):

        if (n1, n2) in used_odds:
            continue

        for n3 in odds[i + j :]:
            if n1 + n2 + n3 == 2020:
                print(n1, n2, n3, n1 * n2 * n3)
                sys.exit()

        used_odds[(n1, n2)] = True


for i, n1 in enumerate(evens):

    for j, n2 in enumerate(evens[i + 1 :]):

        if (n1, n2) in used_evens:
            continue

        for n3 in evens[i + j :]:
            if n1 + n2 + n3 == 2020:
                print(n1, n2, n3, n1 * n2 * n3)
                sys.exit()

        used_evens[(n1, n2)] = True
