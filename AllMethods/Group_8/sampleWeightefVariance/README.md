---------------------------------------------------------------
    sampleWeightedVariance Function
---------------------------------------------------------------

Overview:
---------
- Calculates the weighted variance of a data set using provided weights.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- data (list): A list of numerical data points.
- weights (list): A list of weights corresponding to the data points.

Returns:
--------
- float: The weighted variance of the data set.
- Raises ValueError for mismatched lengths, empty data, zero sum of weights, or insufficient data points.

Functionality:
--------------
- Weighted Variance Calculation: Computes the variance considering the weights of each data point.

Example Usage:
--------------
> data = [1, 2, 3]
> weights = [1, 1, 1]
> result = sampleWeightedVariance(data, weights)
> print(result)  # Output: 1

Error Handling:
---------------
- ValueError: Raised for mismatched lengths, empty data, zero sum of weights, or if there are fewer than two data points.

Test Suite:
-----------
- Tests include weighted variance calculation, handling mismatched lengths, empty data, zero sum of weights, and single element.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
