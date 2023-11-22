import math

def sumOfPowerOfDeviations(data, k, c):
    return sum(math.pow(x - c, k) for x in data)
