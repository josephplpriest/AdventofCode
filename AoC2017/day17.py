nums = [0]

cycles = 366

counter = 1
loc = 0

while counter <= 50000000:

    loc = (cycles+loc) % len(nums) + 1

    nums.insert(loc, counter)

    counter += 1
    
    
print(nums[nums.index(0):])

