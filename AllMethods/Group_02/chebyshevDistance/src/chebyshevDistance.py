def chebyshevDistance(p1, p2):
    if not isinstance(p1, list) or not isinstance(p2, list):
        raise TypeError("Both inputs must be lists")

    if len(p1) != len(p2):
        raise ValueError("Input lists must have the same length")

    return max(abs(a - b) for a, b in zip(p1, p2))
