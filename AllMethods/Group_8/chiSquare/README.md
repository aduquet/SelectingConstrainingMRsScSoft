---------------------------------------------------------------
        chiSquare Function
---------------------------------------------------------------

Overview:
---------
- Computes the chi-square statistic for two lists: expected and observed.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- expected (list): A list of expected values.
- observed (list): A list of observed values.

Returns:
--------
- float: The chi-square statistic.
- Raises TypeError for non-list inputs.
- Raises ValueError for lists of different lengths.

Functionality:
--------------
- Input Validation: Checks if inputs are lists of the same length.
- Rescaling: Rescales expected values if their sum significantly differs from the sum of the observed values.
- Chi-Square Calculation: Computes the chi-square statistic based on expected and observed values.

Example Usage:
--------------
> expected = [10, 20, 30]
> observed = [12, 18, 30]
> result = chiSquare(expected, observed)
> print(result)  # Output: [chi-square statistic]

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths.

Test Suite:
-----------
- Includes tests for typical use cases, invalid input types, and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
