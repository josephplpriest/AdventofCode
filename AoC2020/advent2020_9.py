import sys
##  Part 1  ##

# with open("input9.txt") as file:
#     data = [int(line.strip()) for line in file.readlines()]

# for i in range(25,len(data) - 25):
#     target = data[i]

#     hash_map = {}

#     for num in data[i-25:i]:
#         if hash_map.get(target - num):
#             break
#         else:
#             hash_map[num] = target-num
#             continue
#     else:
        
#         print(f"Sum to {target} not found")
#         break

## Part 2 ##

with open("input9.txt") as file:
    data = [int(line.strip()) for line in file.readlines()]

new_target = 3199139634

for i in range(len(data)):
    
    
    for j in range(i+1, len(data)):
        continuous = data[i:j]
        if sum(continuous) == new_target:
            print(f"Span found between {i} and {j}")
            print(min(data[i:j]) + max(data[i:j]))
            sys.exit()
    


