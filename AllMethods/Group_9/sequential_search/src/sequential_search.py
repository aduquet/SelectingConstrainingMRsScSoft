def sequential_search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return i
    return None
