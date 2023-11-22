---------------------------------------------------------------
    manhattanDistance Function
---------------------------------------------------------------

Overview:
---------
- Calculates the Manhattan distance (L1 distance) between two points.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- p1 (list): The first point in space.
- p2 (list): The second point in space.

Returns:
--------
- int: The Manhattan distance between p1 and p2.
- Raises ValueError if the points have different dimensions.

Functionality:
--------------
- Input Validation: Checks if both points have the same number of dimensions.
- Distance Calculation: Computes the sum of the absolute differences of corresponding coordinates.

Example Usage:
--------------
> point1 = [1, 2, 3]
> point2 = [4, 5, 6]
> result = manhattanDistance(point1, point2)
> print(result)  # Output: 9

Error Handling:
---------------
- ValueError: Raised if the points have different dimensions.

Test Suite:
-----------
- Tests include typical distance calculation and handling of mismatched dimensions.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
