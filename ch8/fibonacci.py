"""Recursion and Dynamic Programming practice.

Translated to Python from Cracking the Coding Interview 6th edition where
indicated.
"""


def fibonacci_exponential(n):
    """Return the nth Fibonacci number. A gross exponential version.

    Translated.

    >>> fibonacci_exponential(5)
    5
    >>> fibonacci_exponential(7)
    13
    >>> fibonacci_exponential(0)
    0
    >>> fibonacci_exponential(1)
    1
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_exponential(n - 1) + fibonacci_exponential(n - 2)


###################################################################
# Improve the runtime with caching. Top-down approach first.
###################################################################

def fibonacci_driver_td(n):
    """A driver for the memoized version of the Fibonacci function.

    Translated.

    >>> fibonacci_driver_td(5)
    5
    >>> fibonacci_driver_td(7)
    13
    >>> fibonacci_driver_td(0)
    0
    >>> fibonacci_driver_td(1)
    1
    """
    cache = {}
    return fibonacci_memo_td(n, cache)


def fibonacci_memo_td(n, cache):
    """Return the nth Fibonacci number using memoization.

    Translated.
    """

    if n == 0 or n == 1:
        return n

    if cache.get(n) is None:
        cache[n] = fibonacci_memo_td(n - 1, cache) + fibonacci_memo_td(n - 2, cache)

    return cache[n]


############################################
# Bottom-up caching approach
############################################

def fib_memo_bu(n):
    """Return the nth Fibonacci number.

    Translated.

    >>> fib_memo_bu(5)
    5
    >>> fib_memo_bu(7)
    13
    >>> fib_memo_bu(0)
    0
    >>> fib_memo_bu(1)
    1
    """

    if n in {0, 1}:
        return n

    cache = {0: 0, 1: 1}

    for i in range(2, n):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n - 1] + cache[n - 2]


#############################################
# Nothin' but variables
#############################################

def fib_variables(n):
    """Return the nth Fibonacci number.

    No cache, no recursion.

    Translated.

    >>> fib_variables(5)
    5
    >>> fib_variables(7)
    13
    >>> fib_variables(0)
    0
    >>> fib_variables(1)
    1
    """

    if n == 0:
        return 0

    if n == 1:
        return 1

    n_minus_2 = 1
    n_minus_1 = 1

    for i in range(3, n):
        curr_fib = n_minus_1 + n_minus_2

        n_minus_1 = n_minus_2
        n_minus_2 = curr_fib

    return n_minus_1 + n_minus_2


if __name__ == "__main__":

    import time

    # Let's time some of this.

    print "Exponential working..."
    print fibonacci_exponential(8)

    nums = range(20)
    for num in nums:
        start_exp = time.time()
        print fibonacci_exponential(num)
        elapsed_exp = (time.time() - start_exp)
        print "Time: {} Numbers calculated: {}".format(elapsed_exp, num + 1)

    print "Memo working..."
    print fibonacci_driver_td(8)

    start_memo = time.time()
    fibonacci_driver_td(50)
    elapsed_memo = (time.time() - start_memo)

    print "Exp: {}".format(elapsed_exp)
    print "Memo: {}".format(elapsed_memo)
