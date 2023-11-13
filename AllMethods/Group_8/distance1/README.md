---------------------------------------------------------------
    distance1 Function
---------------------------------------------------------------

Overview:
---------
- Computes the Manhattan distance (L1 distance) between two points.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- p1 (list or tuple): The first point.
- p2 (list or tuple): The second point.

Returns:
--------
- int/float: The Manhattan distance between p1 and p2.
- Raises TypeError for non-list/tuple inputs.
- Raises ValueError for lists/tuples of different lengths.

Functionality:
--------------
- Input Validation: Ensures both inputs are lists or tuples of the same length.
- Distance Calculation: Computes the sum of absolute differences between corresponding elements of p1 and p2.

Example Usage:
--------------
> point1 = [1, 2, 3]
> point2 = [4, 5, 6]
> result = distance1(point1, point2)
> print(result)  # Output: 9

Error Handling:
---------------
- TypeError: Raised for non-list/tuple inputs.
- ValueError: Raised for lists/tuples of different lengths.

Test Suite:
-----------
- Tests include typical distance calculations, identical points, invalid input types, and mismatched list lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
