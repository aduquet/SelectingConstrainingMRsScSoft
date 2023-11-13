def clip(a, lowerLim, upperLim):
    r = []
    for i in range(len(a)):
        if a[i] < lowerLim:
            r.append(lowerLim)
        elif a[i] > upperLim:
            r.append(upperLim)
        else:
            r.append(a[i])

    return r
