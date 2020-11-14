
def get_parents(family_tree, child_node):
    parents = [node[0] for node in family_tree if node[1] == child_node]

    return parents

def earliest_ancestor(ancestors, starting_node, path = [], visited = set()):
    # ancestors = array of tuples where tuple[0] is the parent and tuple[1] is the child it's connected to

    # find ancestor at farthest disetance from starting_node
    # depth-first search

    # get "neighbors" -- parents on the fly instead of building entire graph up front
    # makes this more dynamic and efficient

    parents = get_parents(ancestors, starting_node)

    # if this is the first function call
    # path is empty
    # "clean" our visited set to be an empty set in case of persisted data from previous tests
    if len(path) == 0:
        visited = set()

    # if the starting_node is the earliest ancestor
    if len(parents) == 0 and len(path) == 0:
        return -1

    if starting_node not in visited:
        visited.add(starting_node)

    path = path + [starting_node]

    if len(parents) == 0:
        return path[-1]
    
    for parent in parents:
        if parent not in visited:
            new_path = earliest_ancestor(ancestors, parent, path, visited)

            if new_path is not None:
                return new_path
