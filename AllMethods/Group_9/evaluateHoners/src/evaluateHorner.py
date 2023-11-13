def evaluateHorner(coefficients, argument):
    n = len(coefficients)
    if n == 0:
        raise ValueError("Coefficient list cannot be empty")

    result = coefficients[n - 1]

    for i in range(n - 2, -1, -1):
        result = argument * result + coefficients[i]

    return result
