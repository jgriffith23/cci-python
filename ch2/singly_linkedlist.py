class LinkedList():
    """A singly linked list, consisting of Nodes that track next.

    Let's make a list. I'm hungry, so it's gonna be fruits.

        >>> fruits = LinkedList()

    Add a node to be the head:

        >>> fruits.append("apple")
        >>> fruits.head
        <Node apple>
        >>> fruits.tail
        <Node apple>

    Now let's add some more:

        >>> fruits.append("berry")
        >>> fruits.tail
        <Node berry>
        >>> fruits.head.next
        <Node berry>
        >>> fruits.tail.prev
        <Node apple>

        >>> fruits.append("cherry")
        >>> fruits.append("dragonfruit")
        >>> fruits.append("eggplant")
        >>> fruits.append("fig")

    I think I want to eat the apple first.

       >>> fruits.remove("apple")

    What's left?

        >>> fruits.display()
        berry
        cherry
        dragonfruit
        eggplant
        fig

    Now a fig.

        >>> fruits.remove("fig")

    What's left?

        >>> fruits.display()
        berry
        cherry
        dragonfruit
        eggplant

    Okay, cherries are awesome.

        >>> fruits.remove("cherry")

    What's left?

        >>> fruits.display()
        berry
        dragonfruit
        eggplant

    Let's save those for later.
 """


    def __init__(self):
        """Initialize an empty LL."""

        self.head = None
        self.tail = None


    def __repr__(self):
        """A human-readable representation of the linked list."""

        return f"<LinkedList Head: {self.head.data} Tail: {self.tail.data}>"


    def append(self, data):
        """Add a new node to the end of the list."""

        new_node = Node(data)

        # Do we have a head yet?
        
        if self.head is None:
            self.head = new_node

        # Do we have a tail yet? If so, we have to make the new node its
        # next and make the new node's previous the current tail, before
        # updating tail to the new node.

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


    def remove(self, data):
        """Remove the node with the given data from the linked list.

        Only remove first occurrence seen.
        """

        if self.head is not None and self.head.data == data:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            return

        # Start at the head.
        current = self.head

        # Iterate over the linked list. If we've hit the end, we can just
        # adjust the tail. Otherwise, we have to move pointers for both
        # nodes around the node to remove.

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next

                if current.next == None:
                    self.tail = current
                return

            else:
                current = current.next


    def display(self):
        """Blat the contents of the list to stdout."""

        current = self.head

        while current is not None:
            print(current.data)

            current = current.next
