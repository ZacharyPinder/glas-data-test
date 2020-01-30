import json
from num2words import num2words

def parent_tree(tree, depth):
    if type(depth) is not int:
        return("Depth must be an int")
    
    output = {}
    parents = []
    in_tree = []
    all_items = []
    layers = 0
    
    if depth == 0:
        return(output)
    
    for item in tree:
        all_items.append(item["id"])
        print(all_items)
        if item["parentId"] is None:
            i =+ 1
            output[num2words(i)] = {"id" : item["id"], "parentId" : None, "children" : []}
            parents.append(item["id"])

    while layers != depth and len(parents) != len(tree):
        for item in tree:
            if item["parentId"] in parents and item["id"] not in parents:
                i += 1
                output[num2words(i)] = {"id" : item["id"], "parentId" : item["parentId"], "children" : []}
                in_tree.append(item["id"])
                for item2 in output.items():
                    if item2[1]["id"] == item["parentId"]:
                        item2[1]["children"].append(item["id"])
        parents = parents + in_tree
        in_tree = []
        layers += 1
    
    return(output)
            

with open("senario/1.json") as file:
    data = json.load(file)

tree = parent_tree(data[0],data[1])
print(tree)