import math

def weightedRMS(data, weights):
    if len(data) != len(weights):
        raise ValueError("Data and weights must have the same length.")

    sumOfSquaredProducts = 0
    sumOfWeights = 0

    for d, w in zip(data, weights):
        sumOfSquaredProducts += d**2 * w
        sumOfWeights += w

    if sumOfWeights == 0:
        raise ValueError("Sum of weights cannot be zero.")

    return math.sqrt(sumOfSquaredProducts / sumOfWeights)
