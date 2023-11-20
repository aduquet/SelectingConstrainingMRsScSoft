def weightedAverage(a, b):
    if len(a) != len(b):
        raise ValueError("Lists 'a' and 'b' must have the same length.")

    sum1, sum2 = 0, 0

    for ai, bi in zip(a, b):
        sum1 += ai * bi
        sum2 += bi

    if sum2 == 0:
        raise ValueError("The sum of weights must not be zero.")

    return sum1 / sum2
