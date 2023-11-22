def checkNonNegative(elements):
    
    if not isinstance(elements, list):
            raise TypeError("Input must be a list")

    # Check if all elements in the list are numeric (int or float)
    for elem in elements:
        if not isinstance(elem, (int, float)):
            raise ValueError(f"Element {elem} is not numeric (int or float)")
        if elem < 0:
            return False
    return True