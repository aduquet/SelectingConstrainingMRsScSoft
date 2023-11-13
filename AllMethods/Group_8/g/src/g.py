import math

def g(expected, observed):
    if not (isinstance(expected, list) and isinstance(observed, list)):
        raise TypeError("Both expected and observed must be lists")

    if len(expected) != len(observed):
        raise ValueError("Expected and observed lists must have the same length")

    sumExpected = sum(expected)
    sumObserved = sum(observed)

    ratio = sumObserved / sumExpected if abs(sumExpected - sumObserved) > 1e-6 else 1

    suma = 0
    for i in range(len(observed)):
        if observed[i] <= 0 or expected[i] <= 0:
            raise ValueError("Observed and expected values must be positive")
        adjusted_expected = ratio * expected[i] if ratio != 1 else expected[i]
        dev = math.log(observed[i] / adjusted_expected)
        suma += observed[i] * dev

    return 2 * suma
