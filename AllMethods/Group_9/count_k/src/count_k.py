def count_k(a, k):
    if not isinstance(a, (list, tuple)):
        raise TypeError("Input must be a list or tuple")

    cnt = 0
    for element in a:
        if element == k:
            cnt += 1

    return cnt
