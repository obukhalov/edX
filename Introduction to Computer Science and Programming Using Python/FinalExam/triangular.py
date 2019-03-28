def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    start = 1
    sum = 1
    while sum <= k:
        if (k - sum) == 0:
            return True
        start += 1
        sum += start

    return False

