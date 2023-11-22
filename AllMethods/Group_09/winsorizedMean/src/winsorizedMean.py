def winsorizedMean(sortedElements, left, right):
    """
    Calculates the Winsorized mean of a sorted list. Winsorization involves replacing a specified number 
    of extreme values from both ends of the data set with the nearest remaining values.

    :param sortedElements: Sorted list of elements.
    :param left: Number of elements to replace from the left end.
    :param right: Number of elements to replace from the right end.
    :return: The Winsorized mean of the list.
    """
    N = len(sortedElements)
    if N == 0:
        return 0  # Handle empty list
    if left + right >= N:
        return sum(sortedElements) / N  # If too many elements are to be replaced, return regular mean

    # Apply Winsorization
    winsorizedList = sortedElements[:]
    if left > 0:
        winsorizedList[:left] = [sortedElements[left]] * left
    if right > 0:
        winsorizedList[-right:] = [sortedElements[-right - 1]] * right

    # Calculate mean
    return sum(winsorizedList) / N
