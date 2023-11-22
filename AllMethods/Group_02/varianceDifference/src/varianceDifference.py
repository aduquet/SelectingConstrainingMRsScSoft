def varianceDifference(sample1, sample2):
    if len(sample1) != len(sample2):
        raise ValueError("Sample sizes must be equal.")

    n = len(sample1)
    if n <= 1:
        raise ValueError("Sample size must be greater than 1.")

    differences = [x - y for x, y in zip(sample1, sample2)]
    mean_diff = sum(differences) / n
    sum_of_squares = sum((d - mean_diff) ** 2 for d in differences)

    return sum_of_squares / (n - 1)
