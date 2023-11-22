def tanimotoDistance(p1, p2):
    ab, aSq, bSq = 0, 0, 0

    for x, y in zip(p1, p2):
        ab += x * y
        aSq += x ** 2
        bSq += y ** 2

    denominator = aSq + bSq - ab
    return 1 - ab / denominator if denominator != 0 else 0
