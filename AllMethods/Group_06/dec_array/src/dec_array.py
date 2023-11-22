def dec_array(a, k):
    if not isinstance(a, list):
        raise TypeError("Input must be a list")
    if not isinstance(k, (int, float)):
        raise TypeError("Decrement value must be a number")

    return [x - k for x in a]
