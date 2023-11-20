def scale(val, arr):
    newArr = []

    for i in range(len(arr)):
        newArr.append(arr[i] * val)

    return newArr
