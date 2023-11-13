def distance1(p1, p2):
    if not (isinstance(p1, (list, tuple)) and isinstance(p2, (list, tuple))):
        raise TypeError("Both inputs must be lists or tuples")

    if len(p1) != len(p2):
        raise ValueError("Input lists must have the same length")

    return sum(abs(a - b) for a, b in zip(p1, p2))
