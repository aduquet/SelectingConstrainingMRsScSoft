import math

def evaluateInternal(x, y, z):
    n = len(x)
    if n == 0:
        raise ValueError("The input lists must not be empty")

    c = [0] * n
    d = [0] * n
    min_dist = math.inf
    nearest = 0

    for i in range(n):
        c[i] = y[i]
        d[i] = y[i]
        dist = abs(z - x[i])
        if dist < min_dist:
            nearest = i
            min_dist = dist

    value = y[nearest]
    for i in range(n):
        for j in range(n - i):
            tc = x[j] - z
            td = x[i + j] - z
            divider = x[j] - x[i + j]
            if divider == 0:
                raise ValueError("Division by zero encountered")
            w = (c[j + 1] - d[j]) / divider
            c[j] = tc * w
            d[j] = td * w

        if 2 * nearest < n - i:
            value += c[nearest]
        else:
            nearest -= 1
            value += d[nearest] if nearest >= 0 else 0

    return value
