def manhattanDistance(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Both points must have the same number of dimensions")

    result = 0
    for i in range(len(p1)):
        result += abs(p1[i] - p2[i])

    return result
