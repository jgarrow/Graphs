
def earliest_ancestor(ancestors, starting_node, path = [], visited = set()):
    # ancestors = array of tuples where tuple[0] is the parent and tuple[1] is the child it's connected to

    # find ancestor at farthest disetance from starting_node
    # depth-first search

    # get "neighbors" -- parents on the fly instead of building entire graph up front
    # makes this more dynamic and efficient

    def get_parents(family_tree, child_node):
        parents = [node[0] for node in family_tree if node[1] == child_node]

        return parents

    parents = get_parents(ancestors, starting_node)

    print(f'starting_node: {starting_node}')
    print(f'parents: {parents}')

    # if the starting_node is the earliest ancestor
    if len(parents) == 0 and len(path) == 0:
        return -1

    if starting_node not in visited:
        visited.add(starting_node)

    path = path + [starting_node]

    if len(parents) == 0:
        print(f'no more parents: {path}')
        return path[-1]
    
    for parent in parents:
        if parent not in visited:
            new_path = earliest_ancestor(ancestors, parent, path, visited)

            if new_path is not None:
                print(f'not none: {new_path}')
                return new_path
    
    
    

