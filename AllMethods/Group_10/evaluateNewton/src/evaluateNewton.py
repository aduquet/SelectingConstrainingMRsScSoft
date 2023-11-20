def evaluateNewton(a, c, z):
    if not (isinstance(a, list) and isinstance(c, list)):
        raise TypeError("Both a and c must be lists")

    if len(a) != len(c) or len(a) == 0:
        raise ValueError("Lists a and c must be of the same non-zero length")

    n = len(c) - 1
    value = a[n]

    for i in range(n - 1, -1, -1):
        value = a[i] + (z - c[i]) * value

    return value
