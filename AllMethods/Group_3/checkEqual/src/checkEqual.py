def checkEqual(a, b):
    if not isinstance(a, (list, tuple)) or not isinstance(b, (list, tuple)):
        raise TypeError("Both inputs must be lists or tuples")

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    return True
