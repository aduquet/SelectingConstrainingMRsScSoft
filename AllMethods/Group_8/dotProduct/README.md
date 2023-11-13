---------------------------------------------------------------
    dot_product Function
---------------------------------------------------------------

Overview:
---------
- Calculates the dot product of two vectors.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list or tuple): The first vector.
- b (list or tuple): The second vector.

Returns:
--------
- int/float: The dot product of vectors a and b.
- Raises TypeError for non-list/tuple inputs.
- Raises ValueError for vectors of different lengths.

Functionality:
--------------
- Input Validation: Checks if inputs are lists or tuples of the same length.
- Calculation: Computes the sum of the products of corresponding elements from a and b.

Example Usage:
--------------
> vector1 = [1, 2, 3]
> vector2 = [4, 5, 6]
> result = dot_product(vector1, vector2)
> print(result)  # Output: 32

Error Handling:
---------------
- TypeError: Raised for non-list/tuple inputs.
- ValueError: Raised for vectors of different lengths.

Test Suite:
-----------
- Tests include typical dot product calculation, empty vectors, invalid input types, and mismatched vector lengths.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
