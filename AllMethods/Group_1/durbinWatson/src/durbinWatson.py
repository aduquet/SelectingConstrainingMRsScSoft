'''
/**
 * Durbin-Watson computation.
 */
public static double durbinWatson(DoubleArrayList data) {
	int size = data.size();
	if (size < 2) throw new IllegalArgumentException("data sequence must contain at least two values.");

	double[] elements = data.elements();
	double run = 0;
	double run_sq = 0;
	run_sq = elements[0] * elements[0];
	for(int i=1; i<size; ++i) {
		double x = elements[i] - elements[i-1];
		run += x*x;
		run_sq += elements[i] * elements[i];
	}

	return run / run_sq;
}
'''

# def durbinWatson(data):
#     size = len(data)


#     elements = data.copy()
#     run = 0
#     run_sq = 0

#     run_sq = elements[0] * elements [0]

#     for i in range(1, len(elements)):
#         x = elements[i] - elements[i - 1]
#         run += x * x
#         run_sq += elements[i] * elements [i]

#     return run/run_sq

def durbinWatson(data):
    if not data:  # check if data is empty
        raise ValueError("Input data should not be empty")

    run = 0
    run_sq = data[0] ** 2

    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]
        run += diff ** 2
        run_sq += data[i] ** 2

    return run / run_sq
