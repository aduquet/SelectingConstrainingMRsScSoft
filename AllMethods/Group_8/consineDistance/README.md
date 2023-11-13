---------------------------------------------------------------
    cosineDistance Function
---------------------------------------------------------------

Overview:
---------
- Computes the cosine distance between two vectors.

Requirements:
-------------
- Python 3.x
- NumPy

Parameters:
-----------
- p1 (list or array): The first vector.
- p2 (list or array): The second vector.

Returns:
--------
- float: Cosine distance between p1 and p2.
- Raises ValueError for vectors of different lengths or empty vectors.

Functionality:
--------------
- Input Validation: Checks if vectors are of the same length and not empty.
- Calculation: Computes the cosine distance as 1 - (dot product / (magnitude of p1 * magnitude of p2)).

Example Usage:
--------------
> vector1 = [1, 0]
> vector2 = [0, 1]
> distance = cosineDistance(vector1, vector2)
> print(distance)  # Output: 1

Error Handling:
---------------
- ValueError: Raised for vectors of different lengths or empty vectors.

Test Suite:
-----------
- Tests include calculations for perpendicular vectors, identical vectors, zero length vectors, and mismatched length vectors.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
