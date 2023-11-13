def set_min_val(a, k):
    for i in range(len(a)):
        if a[i] < k:
            a[i] = k
    return a
