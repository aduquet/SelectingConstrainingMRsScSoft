import math

def sampleSkew(size, moment3, sampleVariance):
    if size < 3:
        raise ValueError("Sample size must be at least 3.")
    if sampleVariance <= 0:
        raise ValueError("Sample variance must be positive.")

    n = size
    s = math.sqrt(sampleVariance)
    m3 = moment3 * n
    return n * m3 / ((n - 1) * (n - 2) * s**3)
