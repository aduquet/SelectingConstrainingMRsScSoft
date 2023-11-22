---------------------------------------------------------------
    check_equal_tolerance Function
---------------------------------------------------------------

Overview:
---------
- Compares two lists or tuples for element-wise equality within a specified tolerance.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list or tuple): First list or tuple for comparison.
- b (list or tuple): Second list or tuple for comparison.
- tol (int or float): Tolerance value for comparison.

Returns:
--------
- bool: Returns True if the elements of a and b are within tol, False otherwise.
- Raises TypeError for invalid input types.

Functionality:
--------------
- Input Validation: Ensures a and b are lists or tuples, and tol is a number.
- Tolerance Check: Compares each element pair within the specified tolerance.

Example Usage:
--------------
> list1 = [1.0, 2.0, 3.0]
> list2 = [1.01, 1.99, 3.0]
> tolerance = 0.05
> result = check_equal_tolerance(list1, list2, tolerance)
> print(result)  # Output: True

Error Handling:
---------------
- TypeError: Raised for invalid input types.

Test Suite:
-----------
- Tests include within tolerance, exceed tolerance, different lengths, and invalid inputs.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
