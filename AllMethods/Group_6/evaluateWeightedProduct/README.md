---------------------------------------------------------------
    evaluateWeightedProduct Function
---------------------------------------------------------------

Overview:
---------
- Calculates the weighted product of a list based on given weights.

Requirements:
-------------
- Python 3.x
- math module

Parameters:
-----------
- values (list): The list of values.
- weights (list): The list of weights corresponding to the values.
- begin (int): The starting index for calculation.
- length (int): The number of elements to include in the calculation.

Returns:
--------
- number: The weighted product of the specified range of values.
- Raises TypeError for non-list inputs.
- Raises ValueError for lists of different lengths.
- Raises IndexError for invalid range specifications.

Functionality:
--------------
- Weighted Product Calculation: Computes the product of values raised to their corresponding weights.

Example Usage:
--------------
> values = [2, 3, 4]
> weights = [1, 0.5, 2]
> begin = 0
> length = 3
> result = evaluateWeightedProduct(values, weights, begin, length)
> print(result)  # Output: 128

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for lists of different lengths.
- IndexError: Raised for invalid range specifications.

Test Suite:
-----------
- Tests include weighted product calculation, invalid range, mismatched list lengths, and invalid input types.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
