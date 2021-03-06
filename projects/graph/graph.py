"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited_verts = set()
        queue = Queue()
        queue.enqueue(starting_vertex)
        
        while queue.size() > 0:
            curr_vert = queue.dequeue()

            if curr_vert not in visited_verts:
                visited_verts.add(curr_vert)
                print(curr_vert)

                neighbors = self.get_neighbors(curr_vert)

                for vert in neighbors:
                    queue.enqueue(vert)

        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use stack
        # keep track of where we've been
        # check very vert once and check every connection once
        stack = Stack()
        stack.push(starting_vertex)

        visited = set()

        # put the start vert into stack
        # while the stack is not empty
        while stack.size() > 0:
            # pop off the top of the stack, this is our current node
            curr_node = stack.pop()

            # check if we have visited this node yet
            # if not, add it to our visited set
            if curr_node not in visited:
                visited.add(curr_node)
                print(curr_node)

                # get each of its neighbors
                # and add them neighbors to our stack
                neighbors = self.get_neighbors(curr_node)

                for vert in neighbors:
                    stack.push(vert)

        

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    # breadth-first search ALWAYS returns the shortest path
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue() # queue of arrays where each array is a path (instead of a queue of vertices)
        queue.enqueue([starting_vertex])
        visited = set()

        if starting_vertex == destination_vertex:
            return

        while queue.size() > 0:
            path = queue.dequeue() # pop first path from queue

            node = path[-1] # get the last node in the path

            if node not in visited:
                neighbors = self.get_neighbors(node)

                # go through all neighbor nodes, construct a new path and
                # push it into the queue
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

                     # return path if neighbor is our destination
                    if neighbor == destination_vertex:
                        return new_path
                    
                # mark node as visited
                visited.add(node)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])

        visited = set()

        if starting_vertex == destination_vertex:
            return
        
        while stack.size() > 0:
            path = stack.pop()

            node = path[-1]

            for neighbor in self.get_neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)

                stack.push(new_path)

                if neighbor == destination_vertex:
                    return new_path
            
            visited.add(node)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)
        
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, path, visited)

                if new_path is not None:
                    return new_path
                



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
