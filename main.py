import json
from num2words import num2words

def parent_tree(tree, depth):
    output = {}
    parents = []
    in_tree = []
    if depth == 0:
        return(output)
    for item in tree:
        if item["parentId"] is None:
            i =+ 1
            output[num2words(i)] = {"id" : item["id"], "parentId" : None, "children" : []}
            parents.append(item["id"])
    for item in tree:
        if item["parentId"] in parents:
            i += 1
            output[num2words(i)] = {"id" : item["id"], "parentId" : item["parentId"], "children" : []}
            in_tree.append(item["id"])
            for item2 in output.items():
                if item2[1]["id"] == item["parentId"]:
                    item2[1]["children"].append(item["id"])
    parents = parents + in_tree
    in_tree = []

    return(output)
            

with open("senario/2.json") as file:
    data = json.load(file)

tree = parent_tree(data[0],data[1])
print(tree)