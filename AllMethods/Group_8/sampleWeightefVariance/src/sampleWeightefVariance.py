def sampleWeightedVariance(data, weights):
    if len(data) != len(weights):
        raise ValueError("Data and weights must be of the same length")

    if len(data) < 2:
        raise ValueError("At least two data points are required")

    sumOfWeights = sum(weights)
    if sumOfWeights == 0:
        raise ValueError("Sum of weights must not be zero")

    sumOfProducts = sum(data[i] * weights[i] for i in range(len(data)))
    sumOfSquaredProducts = sum(data[i] ** 2 * weights[i] for i in range(len(data)))

    weightedVariance = (sumOfSquaredProducts - sumOfProducts ** 2 / sumOfWeights) / (sumOfWeights - 1)
    return weightedVariance
