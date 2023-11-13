---------------------------------------------------------------
    g Function
---------------------------------------------------------------

Overview:
---------
- Calculates a statistic based on expected and observed data lists using logarithmic comparisons.

Requirements:
-------------
- Python 3.x
- math module

Parameters:
-----------
- expected (list): List of expected values.
- observed (list): List of observed values.

Returns:
--------
- float: Calculated statistic based on the inputs.
- Raises TypeError for non-list inputs.
- Raises ValueError for lists of different lengths or non-positive values.

Functionality:
--------------
- Logarithmic Calculation: Computes a statistic involving the logarithm of ratios of observed to expected values.

Example Usage:
--------------
> expected = [1, 2, 3]
> observed = [1, 2, 3]
> result = g(expected, observed)
> print(result)  # Output: 0

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths or non-positive values.

Test Suite:
-----------
- Tests include typical calculation, handling of non-positive values, mismatched list lengths, and invalid input types.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
