"""Implementation of a node.

Useful for trees, linked lists, graphs, etc.
"""


class Node():
    """A node for a linked list.

    Make a node:

        >>> apple = Node("apple")
        >>> apple.data
        'apple'
        >>> print(apple.next)
        None
        >>> print(apple.prev)
        None

    And another:

        >>> berry = Node("berry")
        >>> apple.next = berry
        >>> berry.prev = apple

        >>> print(apple.next)
        <Node berry>
        >>> print(berry.prev)
        <Node apple>
        >>> print(berry.next)
        None
        
    """

    def __init__(self, data):
        """Initialize the node's attributes."""

        self.data = data
        self.next = None
        self.prev = None


    def __repr__(self):
        """A human-readable representation of a node."""

        return f"<Node {self.data}>"


class SinglyLinkedList():
    """A linked list that only goes in one direction. No tail."""

    def __init__(self, head=None):

        self.head = head


    def display(self):
        """Blat the contents of the list to stdout."""

        current = self.head

        while current is not None:
            print(current.data)

            current = current.next


    def reverse(self):
        """Reverse the linked list in place."""

        current = self.head
        prev = None

        while current is not None:
            tmp = current.next
            current.next = prev

            prev = current
            current = tmp

        # Update the head
        self.head = prev


    def get_reversed(self):
        """Return a reversed version of the linked list. Preserve original."""

        next = None
        current = self.head

        while current:
            tmp = Node(current.data)
            tmp.next = next
            next = tmp
            current = current.next

        return SinglyLinkedList(next)

