def triple_step(steps):
    """Calculate the number of ways a child can go up steps.

    A problem from Cracking the Coding Interview 6th Edition.

    A child can hop 1, 2, or 3 steps at a time.

    Assumes combinations are listed like this:

    1 --> (1)
    2 --> (1,1) (2)
    3 --> (1,1,1) (1,2) (2,1) (3)
    4 --> (1,1,1,1) (1,3) (3,1) (2,2) (2,1,1) (1,2,1) (1,1,2)

    etc.

    >>> triple_step(0)
    0

    >>> triple_step(1)
    1

    >>> triple_step(2)
    2

    >>> triple_step(3)
    4

    >>> triple_step(4)
    7

    >>> triple_step(5)
    13

    >>> triple_step(6)
    24
    """

    if steps == 0:
        return 0

    if steps == 1:
        return 1

    if steps == 2:
        return 2

    if steps == 3:
        return 4

    combinations = {0: 0, 1: 1, 2: 2, 3: 4}

    for step_count in range(4, steps + 1):
        combinations[step_count] = (combinations[step_count - 1]
                                    + combinations[step_count - 2]
                                    + combinations[step_count - 3])

    return combinations[steps]

