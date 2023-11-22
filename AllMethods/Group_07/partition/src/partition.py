def partition(work, begin, end, pivot):
    """
    Partitions the list 'work' by placing the element at the pivot index in its correct position in the sorted array,
    and placing all smaller elements to the left of the pivot and all larger elements to the right of the pivot.

    :param work: List of elements to be partitioned.
    :param begin: The starting index of the segment of the list to be partitioned.
    :param end: The ending index (exclusive) of the segment of the list to be partitioned.
    :param pivot: The index of the pivot element.
    :return: The final index position of the pivot element.
    """
    work[pivot], work[begin] = work[begin], work[pivot]
    pivotValue = work[begin]
    i = begin + 1
    for j in range(begin + 1, end):
        if work[j] < pivotValue:
            work[i], work[j] = work[j], work[i]
            i += 1
    work[begin], work[i - 1] = work[i - 1], work[begin]
    return i - 1
