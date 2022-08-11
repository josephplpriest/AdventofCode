with open("input9.txt") as file:
    data = file.read()

data = list(data)[0:200]

i = 0

while i < len(data):

    #cancel chars
    if data[i] == "!":
        del data[i+1]

    i += 1


i = 0

while i < len(data):

    #find garbage

    if data[i] == "<":
        j = i + 1
        while j < len(data):# or data[j] != ">":
            j += 1
        if data[j] == ">":
            del data[i:j+1]

    else:
        i += 1

print(data)