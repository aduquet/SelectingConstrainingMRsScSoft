# def variance(x):
#     suma = 0
#     sum1 = 0
#     var = 0
#     avrg = 0
#     for i in range(0, len(x)):
#         suma = suma + x[i]
#     avrg = suma / len(x)
#     for i in range(0, len(x)):
#         sum1 = sum1 + (x[i] - avrg) * (x[i] - avrg)
#     var = sum1 / len(x)
#     return var


def variance(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")

    if len(data) == 0:
        raise ValueError("List cannot be empty.")

    mean = sum(data) / len(data)
    return sum((i - mean) ** 2 for i in data) / len(data)
