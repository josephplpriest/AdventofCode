# coding: utf-8
get_ipython().run_line_magic('ls', '')
get_ipython().system('cat input_3.txt')
with open("input_3.txt") as file:
    data = file.readlines()
    
data[0:5]
data = [row.strip() for row in data]
data[0:5]
for row in data:
    for col in row:
        
        
        
        
        
        l
        
for row in data:
    l
    
data[0]
len(data[0])
len(data)
col_1_sum = 0
for row in data:
    col_1_sum += int(row[0])
    
col_1_sum
gamma = "0"
epsilon = "1"
import numpy as np
col = []
for row in data:
    for j in row:
        col[j] += 
col = [0]*12]
col = [0]*12
col
for row in data:
    for j in row:
        col[j] += int(row[j])
        
for row in data:
    for j in range(len(row)):
        col[j] += int(row[j])
        
        
col
col > 500
[x>500 for x in col]
[int(x>500) for x in col]
[int(x>500) for x in col]
[int(x<=500) for x in col]
gamma = "".join([str(int(x>500)) for x in col])
gamma
bin(gamma)
bin(int(gamma))
int(gamma)
bin(gamma)
gamma
int(gamma)
help(int)
int(gamma, base=2)
int(epsilon, base=2)
epsilon
epsilon = ''.join([str(int(x<=500)) for x in col])
epsilon
int(epsilon, base=2)
779 * 3316
data
[int(x[0]) for x in data]
sum([int(x[0]) for x in data])
sum([int(x[0]) for x in data])
for i in range(12):
    most_common = str(bool(sum([int(x[i]) for x in data]) < 500))
    
    
for i in range(12):
    most_common = str(int(sum([int(x[i]) for x in data]) < 500))
    data = [row for row in data if row[i] == most_common]
    
    
data
least_common = data.copy()
least_common
with open("input_3.txt") as file:
    data = [row.strip() for row in file.readlines()]
    
data[0:5]
for i in range(12):
    most_common = str(int(sum([int(x[i]) for x in data]) >= 500))
    data = [row for row in data if row[i] == most_common]
    
    
    
data
for i in range(12):
    if sum([int(row[i]) for row in data]) >= len(data)//2:
        most_common = "1"
    else:
        most_common = "0"
    
    data = [row for row in data if row[i] == most_common]  
    
data
with open("input_3.txt") as file:
    data = [row.strip() for row in file.readlines()]
    
data
for i in range(12):
    print(len(data))
    
    if sum([int(row[i]) for row in data]) >= len(data)//2:
        most_common = "1"
    else:
        most_common = "0"
    
    data = [row for row in data if row[i] == most_common]  
    
for i in range(12):
    print(len(data))
    if len(data) == 1:
        break    

    if sum([int(row[i]) for row in data]) >= len(data)//2:
        most_common = "1"
    else:
        most_common = "0"
    
    data = [row for row in data if row[i] == most_common]  
    
with open("input_3.txt") as file:
    data = [row.strip() for row in file.readlines()]
    
for i in range(12):
    print(len(data))
    if len(data) == 1:
        break    

    if sum([int(row[i]) for row in data]) >= len(data)//2:
        most_common = "1"
    else:
        most_common = "0"
    
    data = [row for row in data if row[i] == most_common]  
    
data
with open("input_3.txt") as file:
    data2 = [row.strip() for row in file.readlines()]
    
for i in range(12):
    print(len(data2))
    if len(data2) == 1:
        break    

    if sum([int(row[i]) for row in data2]) >= len(data2)//2:
        most_common = "0"
    else:
        most_common = "1"
    
    data2 = [row for row in data2 if row[i] == most_common]  
    
data2
data, data2
int(data, base=2)
int(data[0], base=2)
int(data2[0], base=2)
1005*3375
get_ipython().run_line_magic('save', '')
