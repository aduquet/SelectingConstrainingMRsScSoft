def get_array_value(array, index):
    """
    Retrieve the element at the specified index from an array.

    Parameters:
    array (list): The array from which to retrieve the value.
    index (int): The index of the element to retrieve, following 1-based indexing.

    Returns:
    The element at the specified index if the index is valid, otherwise None.
    """
    # Adjust index for zero-based indexing
    zero_based_index = index - 1

    # Check if the zero-based index is within the bounds of the array
    if 0 <= zero_based_index < len(array):
        return array[zero_based_index]
    else:
        return None
