def mean_absolute_error(a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        raise TypeError("Both inputs must be lists")

    if len(a) != len(b):
        raise ValueError("Both lists must have the same length")

    if len(a) == 0:
        raise ValueError("Lists must not be empty")

    suma = sum(abs(a[i] - b[i]) for i in range(len(a)))

    return suma / len(a)
