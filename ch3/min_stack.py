"""#3.2 from Cracking the Coding Interview: Stack Min

Design a stack that has a min() method that returns the smallest
element.

.push(), .pop(), and .min() should all be O(1).
"""

from stack import Stack

class MinStack(Stack):
    """A stack that can return its minimum element.

    The only difference between this class and the parent
    is the min functionality. Let's test that.

       >>> nums = MinStack()

    Add a number. Since it's the first one, it should be the smallest.

       >>> nums.push(5)
       >>> nums.min()
       5

    Add a smaller number:

       >>> nums.push(3)
       >>> nums.min()
       3

    Add an even smaller number:

       >>> nums.push(0)
       >>> nums.min()
       0

    Add a number bigger than the last one. The min should stay the same.

       >>> nums.push(1)
       >>> nums.min()
       0

    Pop past the smallest number:

       >>> nums.pop()
       1
       >>> nums.pop()
       0

    Has the min changed?

       >>> nums.min()
       3

    Now pop that. Are we back to the beginning?

       >>> nums.pop()
       3
       >>> nums.min()
       5

    Do we return a reasonable value for an empty stack's min?

       >>> nums.pop()
       5
       >>> print(nums.min())
       None
    """

    def __init__(self):
        super().__init__()
        self.mins = []


    def push(self, item):
        """Place item on top of stack. Update mins as needed."""

        if self.is_empty() or item < self.mins[-1]:
            self.mins.append(item)

        super().push(item)

    def pop(self):
        """Remove item from top of stack and return its value. Update mins."""

        popped_item = super().pop()

        if popped_item == self.mins[-1]:
            self.mins.pop()

        return popped_item

    def min(self):
        """Return the smallest element on the stack."""

        if self.is_empty():
            return None

        else:
            return self.mins[-1]



    
