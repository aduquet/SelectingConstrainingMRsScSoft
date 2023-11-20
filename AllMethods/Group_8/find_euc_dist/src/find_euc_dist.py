import math

def find_euc_dist(a, b):
    if len(a) != len(b):
        raise ValueError("Both lists must have the same length")

    squared_sum = sum((x - y) ** 2 for x, y in zip(a, b))
    return math.sqrt(squared_sum)
