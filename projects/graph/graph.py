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
        if v1 in self.vertices and v2 in self.vertices:
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
        queue = Queue()           # Create empty queue and enqueue the starting_vertex
        visited = set()        # Create an empty set to track visited verticies
        
        queue.enqueue(starting_vertex)           # Add starting vertex to queue

        while queue.size() > 0:               # as long as queue is not empty run code
            popped_vertex = queue.dequeue()         #Take current vertex and pop off the queue
            if popped_vertex not in visited:      #check if it has been visisted if not print it
                print(popped_vertex)
                visited.add(popped_vertex)       #add current vertex to visisted set

            vertex_neighbors = self.get_neighbors(popped_vertex)      #use get neighbors func to get current vertex neighbors

            for n in vertex_neighbors:             #Go through each neighbor
                if n not in visited:      #if neighbor not in visited add it to the queue and we keep going
                    queue.enqueue(n)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)
        while stack.size() > 0:
            popped_vertex = stack.pop()
            if popped_vertex not in visited:
                print(popped_vertex)
                visited.add(popped_vertex)

                vertex_neighbors = self.get_neighbors(popped_vertex)

                for n in vertex_neighbors:
                    if n not in visited:
                        stack.push(n)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        # Create an empty queue and enqueue the PATH TO starting_vertex 
        # Create an empty set to track visited verticies
        # while the queue is not empty:
            # get current vertex PATH (dequeue from queue)
            # set the current vertex to the LAST element of the PATH
            # Check if the current vertex has not been visited:
                
                # CHECK IF THE CURRENT VERTEX IS DESTINATION
                # IF IT IS, STOP AND RETURN
                # Mark the current vertex as visited
                    # Add the current vertex to a visited_set
                # Queue up NEW paths with each neighbor:
                    # take current path
                    # append the neighbor to it
                    # queue up NEW path

        # """
        queue = Queue()
        visited = set()
        
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[len(path) -1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)

            vertex_neighbors = self.get_neighbors(vertex)

            for n in vertex_neighbors:
                copy = list(path)
                copy.append(n)
                queue.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = Stack()
        visited = set()
        
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[len(path) -1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)

            vertex_neighbors = self.get_neighbors(vertex)

            for n in vertex_neighbors:
                copy = list(path)
                copy.append(n)
                queue.enqueue(copy)

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

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
