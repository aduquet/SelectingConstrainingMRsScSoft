import math

def power(data, k):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")

    return [math.pow(x, k) for x in data]
