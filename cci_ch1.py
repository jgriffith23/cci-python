def is_unique(chars):
    """Determine if a string has all unique characters.

    Must use no extra data structures!

    >>> is_unique("foo")
    False

    >>> is_unique("bar")
    True

    >>> is_unique("")
    True

    >>> is_unique("abcdefgg")
    False
    """
    for i in range(len(chars)):
        if chars[i] in chars[i + 1:]:
            return False
    return True

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE CHALLENGE SOLUTIONS!\n"
