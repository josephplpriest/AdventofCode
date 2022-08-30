import numpy as np
import time

with open("input11.txt") as f:
    data = [list(row.strip()) for row in f.readlines()]


data = [int(x) for row in data for x in row]

octopi = np.array(data)

oct = np.reshape(octopi, (10,10))

def dfs(not_oct, row, col):
    start_row = max([0, row-1])
    end_row = min([10, row+2])
    start_col = max([0, col-1])
    end_col = min([10, row+2])
    not_oct[start_row:end_row][start_col:end_col] += 1
    return not_oct

counter = 0

for i in range(100):
    oct += 1
    print(oct)
    print("Sleeping\n\n")
    


    flashed = np.zeros((10,10))


    while np.count_nonzero((oct>=10) - flashed):

        x_and_y = np.where(oct>=10)

        for row, col in zip(x_and_y[0], x_and_y[1]):
            print(flashed)
            time.sleep(1)
            if oct[row][col] >= 10:
                if flashed[row][col] == 0:
                    flashed[row][col] = 1
                    oct = dfs(oct, row, col)
        print(oct)

    print("Flashed: ", np.count_nonzero(flashed))
    oct = np.where(oct >= 10, 0, oct)
    print(oct)
    counter += np.count_nonzero(flashed)

print(counter)