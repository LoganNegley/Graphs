# Given a vertex--starting node-- find the one farthest away from it--farthest ancester--
# More than one earliest ancester return lowest ID ancester
# No parents return -1 ---- no parents=no ancesters

# Make a graph to store the data given
# Go through ancestors to make graph and vertex and edge
# Graph func?

# Make a storage variable for queue
# Start with given node and add to the queue
# bft func?

# if child has no parent return -1
# Or return bft func
# else return current vertex

# While the queue is not empty
# Add starting node to visited set

from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for person in ancestors:
        graph.add_vertex(person[0])
        graph.add_vertex(person[1])
        graph.add_edge(person[1], person[0])
        
    return graph.bft(starting_node)



ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 1))