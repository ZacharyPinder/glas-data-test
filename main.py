import json
from num2words import num2words

def parent_tree(tree, depth):
    if check_data(tree, depth) != 0:
        print(check_data)
    output = {}
    parents = []
    in_tree = []
    layers = 0
    
    if depth == 0:
        return(output)

    for item in tree:
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

def check_data(tree, depth):
    print(len(tree))
    all_items = []
    for item in tree:
        print(item["id"])
        all_items.append(item["id"])
        if item["id"] is not str:
            return("Item id's must be strings")
        if item["parentId"] is not str and item["parentId"] is not None:
            return("parentId must be string or null")
    for item in tree:
        if item["parentId"] not in all_items:
            print(item["parentId"])
            return("One or more items have a parent that does not exist")
    if type(depth) is not int:
        return("Depth must be an interger")
    return(0)
            

with open("senario/4.json") as file:
    data = json.load(file)

tree = parent_tree(data[0],data[1])
print(tree)