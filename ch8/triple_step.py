def triple_step(steps):
    """Calculate the number of ways a child can go up steps.
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



