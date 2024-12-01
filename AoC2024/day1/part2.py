import time
with open("input.txt", mode = 'r') as file:
    data = [x.split() for x in file.readlines()]

nums_a, nums_b = [],[]

for nums in data:
    nums_a.append(int(nums[0]))
    nums_b.append(int(nums[1]))

similarity_total = 0

for i in nums_a:
    i_count = nums_b.count(i)
#    print(i, i_count)
#    time.sleep(.3)
    similarity_total += i * i_count

print(similarity_total)
