# coding: utf-8
get_ipython().run_line_magic('ls', '')
with open("advent2021_input02.txt") as file:
    data = file.readlines()
    
[row.split() for row in data]
[x[0], x[1] for x in row.split() for row in data ]
[(x[0], x[1]) for x in row.split() for row in data ]
[(x[0], x[1]) for row in data for x in row]
[(x[0], x[1]) for row in data for x in row.split()]
[letter for word in row for row in data]
[letter for letter in row for row in data]
data]
data
with open("advent2021_input02.txt") as file:
    data = file.read()
    
data
with open("advent2021_input02.txt") as file:
    data = file.readlines()
    
    
data
data = [row.strip() for row in data]
data
[[x[0][0], int(x[1])) for x in row.split()] for row in data]
[[(x[0][0], int(x[1])) for x in row.split()] for row in data]
[[(x[0], int(y)) for x,y in row.split()] for row in data]
row for row in data
[row for row in data]
[row.split() for row in data]
[[row.split()] for row in data]
[[(x[0], int(y)) for x,y in zip(row.split())] for row in data]
map(data, sum)
map(str.split, data)
print(map(str.split, data))
for row in map(str.split, data):
    print(row)
    
for row in map(str.split, data):
    direction, distance = row[0][0], int(row[1])
    
    
horizontal = 0
vertical = 0
for row in map(str.split, data):
    direction, distance = row[0][0], int(row[1])
    if direction == 'f':
        horizontal += distance
    elif direction == 'd':
        vertical += distance
    else:
        vertical -= distance
        
horizontal, vertical
horizontal * vertical
horizontal = 0
vertical = 0
aim = 0
get_ipython().run_line_magic('save', '')
