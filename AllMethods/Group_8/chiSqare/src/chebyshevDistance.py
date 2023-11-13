def chiSquare(expected, observed):
    if not (isinstance(expected, list) and isinstance(observed, list)):
        raise TypeError("Both expected and observed must be lists")

    if len(expected) != len(observed):
        raise ValueError("Expected and observed lists must have the same length")

    sumExpected = sum(expected)
    sumObserved = sum(observed)

    ratio = sumObserved / sumExpected if abs(sumExpected - sumObserved) > 1e-6 else 1

    sumSq = 0
    for i in range(len(observed)):
        if ratio != 1:
            dev = observed[i] - (ratio * expected[i])
            sumSq += (dev ** 2) / (ratio * expected[i])
        else:
            dev = observed[i] - expected[i]
            sumSq += (dev ** 2) / expected[i]

    return sumSq
