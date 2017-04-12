"""Implements a queue using reqs from Cracking the Coding Interview Ch 3.

Is NOT O(1) for all operations. Need to implement a linked list for that.
"""

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
       <Queue Contains 2 items. Front: Sing -- Pentatonix>
    """

    def __init__(self):
        """Initialize queue."""

        self.items = []


    def __repr__(self):
        """A human-readable representation of the queue instance."""

        return f"<Queue Contains {len(self.items)} items. Front: {self.peek()}>"


    def is_empty(self):
        """Return True if no items in queue. Return False otherwise."""

        return len(self.items) == 0


    def enqueue(self, item):
        """Place an item at the back of the queue."""

        self.items.append(item)


    def dequeue(self):
        """Remove an item from the front of the queue and return it."""

        return self.items.pop(0)


    def peek(self):
        """Check the item at the front of the queue and return its value."""

        return self.items[0]
