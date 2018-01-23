"""CCI 4.2"""


class BinarySearchNode():
    """A node in a binary search tree. Has at most a left and a right child.

    Assume no duplicates in the tree.

    >>> one = BinarySearchNode(1)
    >>> two = BinarySearchNode(2)
    >>> three = BinarySearchNode(3)
    >>> two.insert(one)
    >>> two.insert(three)

    >>> two.get_height()
    2
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<BinarySearchNode data: {self.data}>"

    def insert(self, node):
        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

        elif node.data > self.data:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

        else:
            print("Node could not be inserted. No duplicates.")

    def get_height(self):
        """Return height of tree where this node is the root."""

        def calculate_height(node, height=0):
            """Find the height of a subtree in a BST."""

            if node is None:
                return height

            left_height = calculate_height(node.left, height + 1)
            right_height = calculate_height(node.right, height + 1)

            return left_height if left_height > right_height else right_height

        return calculate_height(self)

    def get_nodes_preorder(self):
        """Get a list of all nodes in the tree with this as the root.

        Preorder visits: root, left, right

        >>> one = BinarySearchNode(1)
        >>> two = BinarySearchNode(2)
        >>> three = BinarySearchNode(3)
        >>> one.left = two
        >>> one.right = three

        >>> one.get_nodes_preorder()
        [1, 2, None, None, 3, None, None]
        """

        visited = [self.data]

        if self.left is None:
            visited.append(None)
        else:
            visited.extend(self.left.get_nodes_preorder())

        if self.right is None:
            visited.append(None)
        else:
            visited.extend(self.right.get_nodes_preorder())

        return visited


def min_bst(values):
    """Create a BST of minimal height from the list of values given.

    >>> t = min_bst([1, 2, 3])
    >>> t.get_height()
    2

    >>> t = min_bst([1, 2, 3, 4, 6, 8, 10])
    >>> t.get_height()
    3

    >>> t = min_bst([4, 12, 13, 25])
    >>> t.get_height()
    3

    >>> t.get_nodes_preorder()
    [13, 12, 4, None, None, None, 25, None, None]
    """

    if len(values) == 1:
        return BinarySearchNode(values[0])

    # Find the root
    midpoint = len(values) // 2
    root = BinarySearchNode(values[midpoint])

    # Split values to create subtrees
    l_vals = values[:midpoint]
    root.insert(min_bst(l_vals))

    if midpoint > 1:
        r_vals = values[midpoint + 1:]
        root.insert(min_bst(r_vals))

    return root
