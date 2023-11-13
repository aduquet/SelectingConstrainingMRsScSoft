def checkEqualTolerance(a, b, tol):
    if not (isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)) and isinstance(tol, (int, float))):
        raise TypeError("First two inputs must be lists or tuples and the third input must be a number")

    if len(a) != len(b):
        return False

    return all(abs(a_elem - b_elem) < tol for a_elem, b_elem in zip(a, b))

