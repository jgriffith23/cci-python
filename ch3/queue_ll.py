"""Implements a queue using reqs from Cracking the Coding Interview Ch 3.

Should be O(1) for all operations.

Philosophical question: Should I be returning Nodes when I dequeue, or
should I be returning the data? I'd argue the data, so the interface
btw the two queue types is the same.
"""

from linkedlist import LinkedList

class Queue():
    """A queue. FIFO.

    Operations: enqueue(item), dequeue(), peek(), is_empty()

    Make a queue:

        >>> karaoke_playlist = Queue()

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
        """Initialize queue."""

        self.items = LinkedList()


    def __repr__(self):
        """A human-readable representation of the queue instance."""

        return f"<Queue Front: {self.peek()}>"


    def is_empty(self):
        """Return True if no items in queue. Return False otherwise."""

        return self.items.head is None 


    def enqueue(self, item):
        """Place an item at the back of the queue."""

        self.items.append(item)


    def dequeue(self):
        """Remove the item at the front of the queue and return it."""

        front_item = self.items.head

        self.items.remove(self.items.head.data)

        return front_item.data


    def peek(self):
        """Check the item at the front of the queue and return it."""

        return self.items.head.data
