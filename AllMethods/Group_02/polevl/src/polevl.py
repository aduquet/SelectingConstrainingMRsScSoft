def polevl(x, coef, N):
    if N >= len(coef):
        raise ValueError("Degree N cannot be greater than or equal to the number of coefficients")

    ans = coef[0]
    for i in range(1, N + 1):
        ans = ans * x + coef[i]

    return ans
