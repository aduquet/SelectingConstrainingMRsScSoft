def weightedMean(elements, theWeights):
    if len(elements) != len(theWeights):
        raise ValueError("Elements and weights must have the same size.")

    total_weighted_sum = sum(e * w for e, w in zip(elements, theWeights))
    total_weight = sum(theWeights)

    if total_weight == 0:
        raise ValueError("Sum of weights cannot be zero.")

    return total_weighted_sum / total_weight

