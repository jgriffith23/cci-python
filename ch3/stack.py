"""Implements a stack using reqs from Cracking the Coding Interview Ch 3."""

class Stack():
    """A stack.

    Operations: pop(), push(item), peek(), is_empty()

    Make a stack:

        >>> stackcats = Stack()

    Anything on the stack?

        >>> stackcats.is_empty()
        True

    Nope! Sadness! Let's stack some cats:

        >>> stackcats.push("Fluffy")
        >>> stackcats.push("Duchess")
        >>> stackcats.push("Annika")
        >>> stackcats.push("Jack")

    Anything there now?

        >>> stackcats.is_empty()
        False

    Yay! Which cat is on top? 

        >>> stackcats.peek()
        Jack

    Let's pet Jack.

        >>> cat_to_pet = stackcats.pop()
        >>> cat_to_pet
        Jack

    Who's next?

       >>> stackcats.peek()
       Annika

    She can wait...a stack of three cats is pretty adorable!
    """

    def __init__(self):
        """Initialize stack."""

        self.items = []


    def __repr__(self):
        """A human-readable representation of the stack insance."""

        return f"<Stack Num items: {len(self.items)} Top: {self.peek()}>"
