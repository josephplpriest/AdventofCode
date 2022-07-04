with open("input_2.txt") as file:
    data = file.read().split(",")

code = 0

data = [int(n) for n in data]
pointer = 0


while (code != 99) or :
    current_input = data[pointer:pointer+4]
    command = current_input[0]

    update_loc = current_input[3]
    loc1 = current_input[1]
    loc2 = current_input[2]


    if command == 1:
        data[update_loc] = sum([data[loc1], data[loc2]])
    elif command == 2:
        data[update_loc] = data[loc1] * data[loc2]
    else:
        print(command)


    #increment the pointer to next command
    pointer += 4

print(data[0])