def errorRate(labels, predictions):
    if not (isinstance(labels, (list, tuple)) and isinstance(predictions, (list, tuple))):
        raise TypeError("Both inputs must be lists or tuples")

    if len(labels) != len(predictions):
        raise ValueError("Labels and predictions lists must have the same length")

    nberrors = 0
    datasize = 0

    for i in range(len(labels)):
        if predictions[i] == -1:
            continue

        if predictions[i] != labels[i]:
            nberrors += 1

        datasize += 1

    if datasize == 0:
        raise ValueError("No valid predictions to evaluate")

    return nberrors / datasize
