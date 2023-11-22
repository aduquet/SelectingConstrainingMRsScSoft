def biSearchFromTo(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2  # Finding the middle element
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return index
        elif mid_value < target:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half

    return -(start + 1)  # Target not found, return negative insertion point

