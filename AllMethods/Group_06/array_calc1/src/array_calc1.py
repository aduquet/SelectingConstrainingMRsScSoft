def array_calc1(r0, i0):
    if i0 == 0:
        raise ValueError("Division by zero is not allowed.")

    if not isinstance(r0, list) or not isinstance(i0, int):
        raise TypeError("Invalid input types.")

    r1 = [0] * len(r0)  # This creates a new array with the same length as r0

    for i in range(len(r0)):
        r1[i] = r0[i] / i0  # Divides each element of r0 by i0 and stores it in r1

    return r1