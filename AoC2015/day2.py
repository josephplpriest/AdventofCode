with open("input2.txt") as file:
    data = file.read()

packages = data.split("\n")

dimensions = []

for row in packages:
    dimensions.append((int(x) for x in row.split("x")))

# part 1
# sizes = []

# for package in dimensions:
#     l,w,h = package
#     s1 = l*w*2
#     s2 = w*h*2
#     s3 = l*h*2
#     smallest = min([s1, s2, s3])
#     sizes.append(sum([s1,s2,s3])+smallest/2)

# print(sum(sizes))

sizes = []

for package in dimensions:
    s,m,l = sorted(package)
    sizes.append(s*m*l + 2*s + 2*m)

print(sum(sizes))