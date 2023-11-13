def quantile(sortedElements, phi):
    if not 0 <= phi <= 1:
        raise ValueError("Quantile phi must be between 0 and 1")

    if len(sortedElements) == 0:
        raise ValueError("List of elements must not be empty")

    n = len(sortedElements)
    index = phi * (n - 1)
    lower_index = int(index)
    fractional_part = index - lower_index

    if lower_index == n - 1:
        return sortedElements[lower_index]
    else:
        return (1 - fractional_part) * sortedElements[lower_index] + fractional_part * sortedElements[lower_index + 1]
