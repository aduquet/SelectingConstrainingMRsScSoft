def hamming_dist(a, b):
    if len(a) != len(b):
        raise ValueError("Inputs must be of the same length")

    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1

    return cnt
