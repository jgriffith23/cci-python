def recursive_multiply(num1, num2):
    """Multiply two numbers in a needlessly complicated fashion.

    >>> recursive_multiply(3, 3)
    9

    >>> recursive_multiply(1, 2)
    2

    >>> recursive_multiply(0, 42)
    0

    >>> recursive_multiply(6, 0)
    0

    >>> recursive_multiply(12, 12)
    144
    """

    if num1 == 1:
        return num2

    if num1 == 0:
        return 0

    else:
        return num2 + recursive_multiply(num1 - 1, num2)

    cache = {}

    if cache.get(num1):
        return cache[num1]
