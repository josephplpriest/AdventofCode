from collections import defaultdict
with open("input8.txt") as f:
    data = f.read()

instructions = data.split("\n")

register = defaultdict(int)

def increment(location, direction, quantity):
    if direction == "inc":
        register[location] += quantity

    else:
        register[location] -= quantity


def update(location:str, direction:str, quantity:int, address, boolean, conditional_val):
    
    address_val = str(register[address])

    conditional_string = " ".join([address_val, boolean, conditional_val])
    
    if eval(conditional_string):
        increment(location, direction, quantity)

largest_seen = 0

for instr in instructions:
    location, direction, quantity, _, address, boolean, conditional_val = instr.split()

    update(location, direction, int(quantity), address, boolean, conditional_val)

    largest = max([v for v in register.values()])

    if largest > largest_seen:
        largest_seen = largest

print(largest_seen)