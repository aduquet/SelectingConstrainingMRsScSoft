def covariance(elements1, elements2):
    if len(elements1) != len(elements2) or len(elements1) == 0:
        raise ValueError("Both lists must be of the same non-zero length")

    size = len(elements1)
    sumx = sum(elements1)
    sumy = sum(elements2)

    meanx = sumx / size
    meany = sumy / size

    sxy = 0
    for i in range(size):
        sxy += (elements1[i] - meanx) * (elements2[i] - meany)

    return sxy / (size - 1)
