'''
/**
 * Returns the product of a data sequence, which is <tt>Prod( data[i] )</tt>.
 * In other words: <tt>data[0]*data[1]*...*data[data.size()-1]</tt>.
 * Note that you may easily get numeric overflows.
 */
public static double product(DoubleArrayList data) {
	int size = data.size();
	double[] elements = data.elements();
	
	double product = 1;
	for (int i=size; --i >= 0;) product *= elements[i];
	
	return product;
}
'''
def product(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list")

    if len(data) == 0:
        raise ValueError("List is empty")

    if not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("List should contain only numbers")

    prod = 1
    for value in data:
        prod *= value

    return prod
