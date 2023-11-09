'''
/**
 * Modifies a data sequence to be standardized.
 * Changes each element <tt>data[i]</tt> as follows: <tt>data[i] = (data[i]-mean)/standardDeviation</tt>.
 */
public static void standardize(DoubleArrayList data, double mean, double standardDeviation) {
	double[] elements = data.elements();
	for (int i=data.size(); --i >= 0;) elements[i] = (elements[i]-mean)/standardDeviation;
}
'''
# import math
# def standardize(data):
#     suma = 0
#     sumSq = 0
#     try:
#         for i in range(0, len(data)):
#             suma += data[i]
#             sumSq += data[i] * data[i]
#         mean = suma / len(data)
#         sd = math.sqrt((sumSq - mean * suma) / len(data))
#         for i in range(0, len(data)):
#             data[i] = (data[i] - mean) / sd
#         return data
#     except:
#         return -11111

import math

def standardize(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")

    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")

    n = len(data)
    if n == 0:
        raise ValueError("List is empty, cannot standardize.")

    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    if std_dev == 0:
        raise ValueError("Standard deviation is zero, cannot standardize.")

    return [(x - mean) / std_dev for x in data]
