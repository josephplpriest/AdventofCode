import time
with open("input.txt", mode = 'r') as file:
    data = file.readlines()

# we have a two lists of numbers

# we want the total difference in indices by pairing sorted values
nums_a, nums_b = [], []


# iteration
for idx, line in enumerate(data):
    int_a, int_b = [int(x) for x in line.split()]

    # iterate through list creating tuples of a, idx_a, b, idx_b
    nums_a.append((int_a, idx))
    nums_b.append((int_b, idx))


# if we sort the two lists of tuples we can just get the total difference between the indices
nums_a.sort(key=lambda x: x[0])
nums_b.sort(key=lambda x: x[0])

total = 0
print(sum([abs(x[0]-y[0]) for x, y in zip(nums_a, nums_b)]))
