import json
from num2words import num2words

def parent_tree(tree, depth):
    # check depth is valid
    if type(depth) is not int:
        return("Depth must be an int")
    
    '''
    output - used to contain output of function
    all_items - ids of all items
    no_parent - ids of items those parent doesn't exist
    no_id - index of items that have no id

    parents - all items that could be parents
    in_tree - all items added to tree this loop
    
    i - used to count items added to output
    layers - used to count layers of tree 
    '''
    output = {}
    all_items = []
    no_id = []
    no_parent = []
    
    parents = []
    in_tree = []
    
    i = 0
    layers = 0

    # return empty id depth == 0
    if depth == 0:
        return(output)

    # find items that do not have an id or parentId key is missing
    for index, item in enumerate(tree):
        if "id" in item:
            if item["id"] is None:
                no_id.append(index)
        else:
            no_id.append(index)
        if "parentId" in item:
            continue
        else:
            no_id.append(index)
    no_id.sort(reverse=True)
    # remove items that do not have an id or are missing parentId key
    for item in no_id:
        tree.pop(item)

    # add the first layer of tree to output
    for item in tree:
        all_items.append(item["id"])
        if item["parentId"] is None:
            i += 1
            output[num2words(i)] = {"id" : item["id"], "parentId" : None, "children" : []}
            parents.append(item["id"])
    for item in tree:
        if item["parentId"] not in all_items and item["parentId"] is not None:
            no_parent.append(item["id"])

    # add layers to tree
    while layers != depth and (len(parents) + len(no_parent)) < len(tree):
        for item in tree:
            if item["parentId"] in parents and item["id"] not in parents:
                i += 1
                output[num2words(i)] = {"id" : item["id"], "parentId" : item["parentId"], "children" : []}
                in_tree.append(item["id"])
                for find_parent in output.items():
                    if find_parent[1]["id"] == item["parentId"]:
                        find_parent[1]["children"].append(item["id"])
            # if an items parent is in no_parent it also needs to be added
            if item["parentId"] in no_parent:
                no_parent.append(item["id"])
        parents += in_tree
        in_tree = []
    return(output)
            

with open("senario/5.json") as file:
    data = json.load(file)

tree = parent_tree(data[0],data[1])
print(tree)