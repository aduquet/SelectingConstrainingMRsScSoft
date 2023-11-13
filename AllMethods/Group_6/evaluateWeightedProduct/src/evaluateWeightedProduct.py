import math

def evaluateWeightedProduct(values, weights, begin, length):
    if not (isinstance(values, list) and isinstance(weights, list)):
        raise TypeError("Both values and weights must be lists")

    if len(values) != len(weights):
        raise ValueError("Values and weights lists must be of the same length")

    if begin < 0 or length < 0 or (begin + length) > len(values):
        raise IndexError("Invalid range specified")

    product = 1
    for i in range(begin, begin + length):
        product *= math.pow(values[i], weights[i])

    return product
