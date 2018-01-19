"""CCI 4.12

   Given a binary tree in which each node contains an int, count num paths that
   sum to a given value. Can start anywhere but must go down.
"""


class BinaryNode(object):
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        if self.left is None and self.right is None:
            return f"<Node {self.data}>"
        else:
            return f"<Node {self.data} l={self.left.data} r={self.right.data}>"


def paths_w_sum(tree, num):
    """Determine how many ways you can add nodes to a sum.

       >>> one = BinaryNode(1)
       >>> three = BinaryNode(3)
       >>> two_1 = BinaryNode(2)
       >>> two_2 = BinaryNode(2)
       >>> five = BinaryNode(5)

       >>> one.left = three
       >>> one.right = two_1
       >>> two_1.left = two_2
       >>> two_1.right = five

       >>> print(paths_w_sum(one, 4))
       2

       >>> ten = BinaryNode(10)
       >>> five_2 = BinaryNode(5)
       >>> three_2 = BinaryNode(3)
       >>> three_3 = BinaryNode(3)
       >>> neg_two = BinaryNode(-2)
       >>> two_3 = BinaryNode(2)
       >>> neg_three = BinaryNode(-3)
       >>> one_2 = BinaryNode(1)
       >>> eleven = BinaryNode(11)

       >>> ten.left = five_2
       >>> ten.right = neg_three
       >>> five_2.left = three_2
       >>> five_2.right = two_3
       >>> three_2.left = three_3
       >>> three_2.right = neg_two
       >>> two_3.right = one_2
       >>> neg_three.right = eleven

       >>> print(paths_w_sum(ten, 8))
       3
       >>> print(paths_w_sum(ten, 7))
       2
       >>> print(paths_w_sum(ten, 42))
       0
       >>> print(paths_w_sum(ten, -3))
       1
    """

    def find_paths(node, num, curr_sum):
        if node is None:
            return 0

        paths = 0
        curr_sum += node.data

        if curr_sum == num:
            paths += 1

        paths_left = find_paths(node.left, num, curr_sum)
        paths_right = find_paths(node.right, num, curr_sum)

        paths += paths_left + paths_right

        return paths

    if tree is None:
        return 0

    sums_starting_here = find_paths(tree, num, 0)
    sums_starting_left = paths_w_sum(tree.left, num)
    sums_starting_right = paths_w_sum(tree.right, num)

    total = sums_starting_here + sums_starting_right + sums_starting_left

    return total
