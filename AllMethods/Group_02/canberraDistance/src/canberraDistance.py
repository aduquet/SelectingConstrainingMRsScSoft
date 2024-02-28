import numpy as np

def canberraDistance(x, y):
    """
    Compute the Canberra distance between two vectors x and y.
    
    Parameters:
        x, y: array_like
            Input arrays.
    
    Returns:
        float
            The Canberra distance between vectors x and y.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    
    # Check if the lengths of the input arrays are equal
    if len(x) != len(y):
        raise ValueError("Input arrays must have the same length")
    
    # Compute Canberra distance
    numerator = np.abs(x - y)
    denominator = np.abs(x) + np.abs(y)
    canberra_dist = np.sum(numerator / denominator)
    
    return canberra_dist
