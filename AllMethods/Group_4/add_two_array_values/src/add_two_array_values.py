def add_two_array_values(a, i, j):
    if not isinstance(a, (list, tuple)):
        raise TypeError("The first argument must be a list or tuple.")
    if not isinstance(i, int) or not isinstance(j, int):
        raise TypeError("The second and third arguments must be integers.")
    if i < 0 or i >= len(a) or j < 0 or j >= len(a):
        raise IndexError("Index out of bounds.")
    else:
        return a[i] + (a[j] / 2)
