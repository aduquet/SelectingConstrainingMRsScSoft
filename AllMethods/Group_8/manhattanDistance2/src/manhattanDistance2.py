def manhattanDistance2(array1, array2):
    """
    Calculates the Manhattan distance between two points represented as integer arrays, using a traditional approach.

    :param array1: The first point as an integer array.
    :param array2: The second point as an integer array.
    :return: The Manhattan distance as a float.
    :raises ValueError: If the lengths of the input arrays are not equal.
    """
    if len(array1) != len(array2):
        raise ValueError("Both arrays must have the same length")

    # Declare all auxiliary variables first
    distance = 0.0
    diff = 0
    abs_diff = 0
    i = 0
    length = len(array1)

    # Calculate the Manhattan distance using a traditional loop
    while i < length:
        diff = array1[i] - array2[i]
        abs_diff = abs(diff)
        distance += abs_diff
        i += 1

    return float(distance)
