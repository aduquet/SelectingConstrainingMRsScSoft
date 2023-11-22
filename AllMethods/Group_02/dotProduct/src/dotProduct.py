def dotProduct(a, b):
    if not (isinstance(a, (list, tuple)) and isinstance(b, (list, tuple))):
        raise TypeError("Both inputs must be lists or tuples")

    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    return sum(x * y for x, y in zip(a, b))
