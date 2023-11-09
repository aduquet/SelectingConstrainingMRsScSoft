'''
/**
 * Returns the sum of logarithms of a data sequence, which is <tt>Sum( Log(data[i])</tt>.
 * @param data the data sequence.
 * @param from the index of the first data element (inclusive).
 * @param to the index of the last data element (inclusive).
 */
public static double sumOfLogarithms(DoubleArrayList data, int from, int to) {
	double[] elements = data.elements();
	double logsum = 0;
	for (int i=from-1; ++i <= to;) logsum += Math.log(elements[i]);
	return logsum;
}
'''
# import math
# def sumOfLogarithms(data, froom, to):
#     elements = data.copy()
#     logsum = 0
#     for i in range(froom - 1, len(elements)):
#         logsum += math.log(elements[i])
#     return logsum
# def sumOfLogarithms(elements):
#     logsum = 0
#     for i in range(0, len(elements)):
#         logsum += math.log(elements[i])
#     return logsum

import math

def sumOfLogarithms(elements):
    if not isinstance(elements, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in elements):
        raise ValueError("List should contain only numbers.")

    if any(i <= 0 for i in elements):
        raise ValueError("All numbers in the list should be positive to compute the logarithm.")

    return sum(math.log(element) for element in elements)
