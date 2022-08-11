import sys
with open("input7.txt") as file:
    data = file.readlines()


discs = [row.strip().split(" -> ") for row in data]


nodes = dict()

for disc in discs:

    name, weight = disc[0].split(" (")

    weight = int(weight.strip(")"))

    #node name
    nodes[name] = {"weight": weight}


    #node children or none
    if len(disc) == 2:
        children = disc[1].split(", ")
        
        nodes[name]["children"] = children
    else:
        nodes[name]["children"] = None
        nodes[name]["total"] = nodes[name]["weight"]

def get_weights(node):
    if nodes[node]["children"] == None:
        return nodes[node]["weight"]
    else:
        child_weights = [get_weights(name) for name in nodes[node]["children"]]
        
        if len(set(child_weights)) != 1:
            print("\n\n", node, nodes[node]["weight"], nodes[node]["children"], child_weights)
        
        return nodes[node]["weight"] + sum(child_weights)

weights_dict = {}

for k in nodes:
    if nodes[k]["children"] == None:
        weights_dict[k] = nodes[k]["weight"]
    else:
        weights_dict[k] = get_weights(k)

