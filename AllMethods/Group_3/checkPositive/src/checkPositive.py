def checkPositive(elements):
    if not isinstance(elements, list):
        raise TypeError("Input must be a list")

    for elem in elements:
        if not isinstance(elem, (int, float)):
            raise ValueError("All elements in the list must be either integers or floats")
        if elem <= 0:
            return False

    return True
