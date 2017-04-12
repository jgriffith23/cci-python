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
       >>> nums.push(5)
       >>> nums.min()
       5
       >>> nums.push(3)
       >>> nums.min()
       3
       >>> nums.push(0)
       >>> nums.min()
       0
       >>> nums.push(1)
       >>> nums.min()
       0
       >>> nums.pop()
       1
       >>> nums.pop()
       0
       >>> nums.min()
       3
       >>> nums.pop()
       3
       >>> nums.min()
       5
       >>> nums.pop()
       5
       >>> print(nums.min())
       None
    """

    def __init__(self):
        super().__init__()
        self.mins = []

    
