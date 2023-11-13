import numpy as np

def cosineDistance(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Vectors must be of the same length")

    if len(p1) == 0 or len(p2) == 0:
        raise ValueError("Vectors must not be empty")

    dotProduct = np.dot(p1, p2)
    lengthSquaredp1 = np.dot(p1, p1)
    lengthSquaredp2 = np.dot(p2, p2)

    denominator = np.sqrt(lengthSquaredp1) * np.sqrt(lengthSquaredp2)

    if denominator == 0:
        return 0

    return 1 - dotProduct / denominator
