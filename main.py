import json

def parent_tree(tree, depth):
    print(tree)

with open("senario/1.json") as file:
    data = json.load(file)

parent_tree(data,1)