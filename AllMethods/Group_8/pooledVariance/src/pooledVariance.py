def pooledVariance(data1, data2):
    if len(data1) == 0 or len(data2) == 0:
        raise ValueError("Data sets must not be empty")

    mean1 = sum(data1) / len(data1)
    var1 = sum((x - mean1) ** 2 for x in data1) / len(data1)

    mean2 = sum(data2) / len(data2)
    var2 = sum((x - mean2) ** 2 for x in data2) / len(data2)

    pooled_var = (len(data1) * var1 + len(data2) * var2) / (len(data1) + len(data2))
    return pooled_var
