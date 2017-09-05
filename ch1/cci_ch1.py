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

    If we could use other data structures, this could also:
    - Turn the string into a set and compare its length with the string's length.
    - Keep a "seen" list, and compare its length with the string's length.
    - Use a dictionary to count; if a count goes higher than 1, return False.
    """
    for i in range(len(chars)):
        if chars[i] in chars[i + 1:]:
            return False
    return True


def is_permutation(string1, string2):
    """Given two strings, determine whether one is a permutation of the other.

    >>> is_permutation('hackbright', 'ghtribckha')
    True

    >>> is_permutation('dog', 'ogd')
    True
    """

    print "FINISH THIS"

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE CHALLENGE SOLUTIONS!***\n"
