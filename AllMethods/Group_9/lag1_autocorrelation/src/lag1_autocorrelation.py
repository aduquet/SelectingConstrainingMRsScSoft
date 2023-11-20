def lag1_autocorrelation(elements, mean):
    v = (elements[0] - mean) ** 2
    q = 0
    for i in range(len(elements)):
        delta0 = elements[i - 1] - mean if i > 0 else 0
        delta1 = elements[i] - mean

        q = q + (delta0 * delta1 - q) / (i + 1)
        v = v + (delta1 ** 2 - v) / (i + 1)

    return q / v if v != 0 else 0
