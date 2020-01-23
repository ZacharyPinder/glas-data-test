import json
from num2words import num2words

def parent_tree(tree, depth):
    output ={}
    if depth == 0:
        return(output)
    for item in tree:
        if item["parentId"] is None:
            i =+ 1
            output[num2words(i)] = {"id" : item["id"], "parentId" : None, "children" : []}
    

    print(output)
            

with open("senario/2.json") as file:
    data = json.load(file)

parent_tree(data[0],data[1])