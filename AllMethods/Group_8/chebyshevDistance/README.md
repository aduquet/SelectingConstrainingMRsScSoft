---------------------------------------------------------------
        chebyshevDistance Function
---------------------------------------------------------------

Overview:
---------
- Calculates the Chebyshev distance between two points represented as lists.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- p1 (list): The first point (list of coordinates).
- p2 (list): The second point (list of coordinates).

Returns:
--------
- int/float: The Chebyshev distance between p1 and p2.
- Raises TypeError for non-list inputs.
- Raises ValueError if lists have different lengths.

Functionality:
--------------
- Input Validation: Checks if both p1 and p2 are lists of the same length.
- Distance Calculation: Computes the Chebyshev distance, defined as the maximum absolute difference between coordinates of the two points.

Example Usage:
--------------
> point1 = [1, 2, 3]
> point2 = [4, 5, 6]
> distance = chebyshevDistance(point1, point2)
> print(distance)  # Output: 3

Error Handling:
---------------
- TypeError: Raised if inputs are not lists.
- ValueError: Raised if lists have different lengths.

Test Suite:
-----------
- Includes tests for normal cases, single-dimensional inputs, non-list inputs, and mismatched lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
