import re

# read in the input
with open("input7.txt") as file:
    data = [line for line in file.read().split("\n")]

# split the input into lines
regex = re.compile(r"[0-9] ")


# create an empty dict for valid bags
valid_bag_lookup = {}

is_valid = {}

# create a lookup dict which will have a bag as a key and tuple of bags it can hold as values
bag_contains = [row.split(" contain ") for row in data]

for line in bag_contains:
    outer_bag = " ".join(line[0].split(" ")[0:2])

    if line[1] == "no other bags.":
        is_valid[outer_bag] = False

    else:
        contained_bags = re.split(regex, line[1])
        contained_bags = [
            " ".join(item.strip().split()[0:2]) for item in contained_bags
        ]
        valid_bag_lookup[outer_bag] = tuple(contained_bags[1:])


# iterate through each line of file
def bag_checker(lookup_key):
    if valid_bag_lookup.get(lookup_key) == None:
        return False
    elif len(set(valid_colors).intersection(set(valid_bag_lookup[lookup_key]))) > 0:
        is_valid[lookup_key] = True
        return True
    for bag in valid_bag_lookup[lookup_key]:
        bag_checker(bag)


valid_colors = ["shiny gold"]

# add bag to lookup dict
while len(is_valid.items()) < 584:
    for i, item in enumerate(valid_bag_lookup):

        if bag_checker(item):
            valid_colors.append(item)
