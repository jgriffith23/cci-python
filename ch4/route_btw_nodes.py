"""CCI #4.1
   Given a directed graph, design an algorithm to find out whether there is
   a route between two nodes.
"""


class Node():
    """A vertex in a directed graph.

    >>> berry = Node("berry")
    >>> cherry = Node("cherry")
    >>> durian = Node("durian")
    >>> berry.add_neighbor(cherry)
    >>> apple = Node("apple", {berry, durian})
    >>> sorted(apple.adjacent)
    [<Node data: berry>, <Node data: durian>]
    >>> berry.adjacent
    {<Node data: cherry>}
    >>> cherry.adjacent
    set()
    >>> durian.adjacent
    set()
    """

    def __init__(self, data, adjacent=None):
        self.data = data
        if adjacent is not None:
            self.adjacent = adjacent
        else:
            self.adjacent = set([])

    def add_neighbor(self, node):
        """Give a node a new neighbor."""

        self.adjacent.add(node)

    def __repr__(self):
        return f"<Node data: {self.data}>"

    def __lt__(self, other_node):
        if other_node.data < self.data:
            return False
        else:
            return True


class DirectedGraph():
    """A graph where connections are one-way streets.

    >>> berry = Node("berry")
    >>> cherry = Node("cherry")
    >>> durian = Node("durian")
    >>> berry.add_neighbor(cherry)
    >>> apple = Node("apple", {berry, durian})

    >>> fruits = DirectedGraph({apple, berry, cherry, durian})
    >>> fruits
    <DirectedGraph (4 nodes)>

    Recursive connection, df:
    >>> fruits.are_connected_rec(berry, cherry)
    (True, 1)
    >>> fruits.are_connected_rec(apple, berry)
    (True, 1)
    >>> fruits.are_connected_rec(apple, cherry)
    (True, 2)

    Remember, the graph is directed.
    >>> fruits.are_connected_rec(berry, apple)
    (False, None)

    Theoretically, a node could be connected to itself.
    >>> fruits.are_connected_rec(durian, durian)
    (True, 0)

    Iterative, still df:
    >>> fruits.are_connected_it(apple, berry)
    True
    >>> fruits.are_connected_it(apple, cherry)
    True
    >>> fruits.are_connected_it(durian, apple)
    False
    >>> fruits.are_connected_it(berry, durian)
    False
    >>> fruits.are_connected_it(cherry, cherry)
    True
    """

    def __init__(self, nodes=None):
        if nodes is not None:
            self.nodes = nodes

        else:
            self.nodes = set([])

    def __repr__(self):
        return f"<DirectedGraph ({len(self.nodes)} nodes)>"

    def are_connected_rec(self, node1, node2, degrees=0, seen=None):
        """DF check for connection between nodes. Return degrees separated."""

        if seen is None:
            seen = set([])

        if node1 is node2:
            return (True, degrees)

        seen.add(node1)

        for node in node1.adjacent:
            if node is node2:
                return (True, degrees + 1)

            connection = self.are_connected_rec(
                node,
                node2,
                degrees=degrees + 1,
                seen=seen
            )

            if connection[0] is True:
                return connection

        return (False, None)

    def are_connected_it(self, node1, node2):
        """DF check for connection between nodes. Return T/F."""

        to_visit = [node1]
        seen = set([])

        while to_visit:
            # pop from front/use a queue class to get BFS
            current = to_visit.pop()
            seen.add(current)

            if current is node2:
                return True

            else:
                to_visit.extend(current.adjacent - seen)

        return False

    
