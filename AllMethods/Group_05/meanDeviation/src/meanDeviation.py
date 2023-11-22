def meanDeviation(elements, mean):
    if not isinstance(elements, list):
        raise TypeError("Elements must be a list")

    size = len(elements)
    if size == 0:
        raise ValueError("Elements list cannot be empty")

    suma = sum(abs(element - mean) for element in elements)

    return suma / size
