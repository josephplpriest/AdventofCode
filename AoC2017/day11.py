with open("input11.txt") as file:
    data = file.read()

steps = data.split(",")

up_down = 0

ne_sw = 0

se_nw = 0

for s in steps:
    if s == "n":
        up_down += 1
    elif s == "s":
        up_down -= 1
    elif s == "ne":
        ne_sw += 1
    elif s == "sw":
        ne_sw -= 1
    elif s == "nw":
        se_nw += 1
    else:
        se_nw -= 1

print(up_down, ne_sw, se_nw)