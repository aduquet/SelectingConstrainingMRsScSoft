def sampleKurtosis(size, moment4, sampleVariance):
    if size < 4:
        raise ValueError("Sample size must be at least 4.")
    if sampleVariance <= 0:
        raise ValueError("Sample variance must be positive.")

    n = size
    s2 = sampleVariance
    m4 = moment4
    term1 = m4 * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * s2 * s2)
    term2 = 3.0 * (n - 1) * (n - 1) / ((n - 2) * (n - 3))

    return term1 - term2
