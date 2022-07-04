storage_dict = {}

with open("input14.txt") as file:
    data = file.read().split("\n")

data = [line.split(" ") for line in data]



for i, line in enumerate(data):
    if line[0] == "mask" and i == 0:
        mask = line[2]
    elif line[0] == "mask":
        updated_mask = ""
        for old, new in zip(mask, line[2]):
            if new == "X":
                updated_mask += old
            elif new == "1":
                updated_mask += new
            else:
                updated_mask += new
        mask = updated_mask

    else:
        location = line[0][4:-1]
        int32_number = line[2]
        print(mask, location, int32_number)


        input_number = '{:032b}'.format(int(int32_number))

        num = ""

        for m, n in zip(mask, input_number):
            if m == "X":
                num += n
            elif m == n:
                num += n
            else:
                num += m
        print(int(num, base=2))
        storage_dict[location] = int(num, base=2)

final_nums = []

for key in storage_dict:
    final_nums.append(storage_dict[key])

print(sum(final_nums))