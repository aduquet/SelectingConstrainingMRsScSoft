def sampleVariance(elements, mean):
    if len(elements) < 2:
        raise ValueError("At least two elements are required to calculate sample variance")

    size = len(elements)
    suma = 0

    for i in range(size):
        delta = elements[i] - mean
        suma += delta * delta

    return suma / (size - 1)
