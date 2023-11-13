def meanDifference(sample1, sample2):
    if not (isinstance(sample1, list) and isinstance(sample2, list)):
        raise TypeError("Both inputs must be lists")

    if len(sample1) != len(sample2):
        raise ValueError("Both samples must have the same length")

    if len(sample1) == 0:
        raise ValueError("Samples must not be empty")

    sumDifference = sum(sample1[i] - sample2[i] for i in range(len(sample1)))

    return sumDifference / len(sample1)
