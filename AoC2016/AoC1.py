with open("input1.txt") as file:
    data = file.read()

data = data.split(", ")

print(data[1])

vectors = {"N": 0, "S": 0, "E": 0, "W": 0}

update = {
    "N": {"R": "E", "L": "W"},
    "S": {"R": "W", "L": "E"},
    "E": {"L": "N", "R": "S"},
    "W": {"L": "S", "R": "N"},
}

current_loc = (0, 0)
current_direction = "N"

for instruct in data:
    print(instruct)
    letter = instruct[0]
    distance = int(instruct[1])

    # update direction
    current_direction = update[current_direction][letter]

    # add quantity of input
    vectors[current_direction] += distance

    x, y = current_loc
    if current_direction == "N":

        current_loc = (x, y + distance)

    elif current_direction == "S":
        current_loc = (x, abs(y - distance))

    elif current_direction == "E":
        current_loc = (x + distance, y)

    else:
        current_loc = (abs(x - distance), y)

    print(vectors, current_loc)


print(current_loc)
