'''
Returns the smallest member of a data sequence.

JAVA VERSION
public static double min(DoubleArrayList data) {
	int size = data.size();
	if (size==0) throw new IllegalArgumentException();
	
	double[] elements = data.elements();
	double min = elements[size-1];
	for (int i = size-1; --i >= 0;) {
		if (elements[i] < min) min = elements[i];
	}

	return min;
}'''

def min(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list")

    if len(data) == 0:
        raise ValueError("List is empty, cannot determine minimum")

    if not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("List should contain only numbers")

    min_val = data[0]
    for value in data:
        if value < min_val:
            min_val = value

    return min_val
