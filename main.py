import json

def parent_tree(tree, depth):
    for item in tree:
        if item["parentId"] is None:
            print("none")

with open("senario/1.json") as file:
    data = json.load(file)

parent_tree(data[0],data[1])