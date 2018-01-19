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

    >>> is_permutation("apple", "berry")
    False

    Runtime: O(m + n), where m is len(string1) and n is len(string2)
    """

    if len(string1) != len(string2):
        return False

    sorted_str1 = sorted(string1)
    sorted_str2 = sorted(string2)

    return sorted_str1 == sorted_str2


def urlify(query, length):
    """CCI 1.3

    Replace all spaces in a string with %20.

    >>> urlify("Mr John Smith    ", 13)
    'Mr%20John%20Smith'
    """

    chars = query.strip().split(" ")
    return "%20".join(chars)


def is_palindrome_permutation(string):
    """CCI 1.4

    Given a string, check if it is a permutation of a palindrome.

    >>> is_palindrome_permutation("Tact Coa")
    True

    >>> is_palindrome_permutation("dog")
    False

    >>> is_palindrome_permutation("total")
    False

    >>> is_palindrome_permutation("toott")
    True

    (Permutations: "taco cat", "atco cta", etc)
    """

    odd_found = False
    curr_count = 0
    curr_char = None

    for char in sorted(string.lower()):
        if char == " ":
            continue

        if char != curr_char:
            curr_char = char

            if curr_count % 2 != 0 and odd_found:
                return False

            elif curr_count % 2 != 0:
                odd_found = True

            curr_count = 1

        else:
            curr_count += 1

    return True


def compress(string):
    """CCI 1.6

    Compress a string using repeated character counts.

    >>> compress("aabcccccaaa")
    'a2b1c5a3'

    If compressed string isn't smaller, return original.

    >>> compress("dog")
    'dog'

    >>> compress("aabbcc")   # a2b2c2 is same length
    'aabbcc'
    """

    curr_char = string[0]
    curr_count = 1

    out = []

    for char in string[1:]:
        if char == curr_char:
            curr_count += 1
        else:
            out.append(curr_char)
            out.append(str(curr_count))

            curr_char = char
            curr_count = 1

    out.extend([curr_char, str(curr_count)])

    if len(out) >= len(string):
        return string

    return "".join(out)


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE CHALLENGE SOLUTIONS!***\n")
