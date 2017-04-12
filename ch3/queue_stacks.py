"""#3.4 in Cracking the Coding Interview: Implement a queue w/ two stacks."""

from stack import Stack

class StackedQueue():
    """A queue that uses two stacks.

    Operations: enqueue(item), dequeue(), peek(), is_empty()

    Make a queue:

        >>> karaoke_playlist = StackedQueue()

    Anything in the queue?

        >>> karaoke_playlist.is_empty()
        True

    If there's nothing in the karaoke queue, how can we sing like crazy
    people? Let's add songs.

        >>> karaoke_playlist.enqueue("Try Everything -- Shakira")
        >>> karaoke_playlist.enqueue("Sing -- Pentatonix")
        >>> karaoke_playlist.enqueue("Best Day of My Life -- American Authors")

    Anything in the queue now?

       >>> karaoke_playlist.is_empty()
       False

    Sweeeet. Now we can belt some tunes. Which song is first?

       >>> karaoke_playlist.peek()
       'Try Everything -- Shakira'

    Let's sing it!

       >>> song = karaoke_playlist.dequeue()

    Are we singing the right song?

       >>> print(f"Now singing: {song}")
       Now singing: Try Everything -- Shakira

    Looks about right. What's next?

       >>> karaoke_playlist.peek()
       'Sing -- Pentatonix'

    We can take a break now...

    But let's see how our repr comes out, anyway.

       >>> print(karaoke_playlist)
       <Queue Front: Sing -- Pentatonix>
    """


    def __init__(self):
        """Initialize the queue and its attributes."""

        self.out_stack = Stack()
        self.in_stack = Stack()


    def __repr__(self):
        """A human-readable representation of this weird queue."""

        return f"<Queue Front: {self.peek()}>"


    def is_empty(self):
        """Return True if no items in queue. Return False otherwise."""

        return self.out_stack.is_empty() and self.in_stack.is_empty()


    def enqueue(self, item):
        """Place an item at the back of the queue."""

        self.in_stack.push(item)


    def dequeue(self):
        """Remove item at front of queue and return its value."""

        if self.out_stack.is_empty():
            self.flip_in_stack()

        return self.out_stack.pop()


    def flip_in_stack(self):
        """Turn the stack we've been pushing items onto upside down."""

        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())


    def peek(self):
        if self.out_stack.is_empty():
            self.flip_in_stack()

        return self.out_stack.peek()
