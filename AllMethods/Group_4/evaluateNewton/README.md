---------------------------------------------------------------
    evaluateNewton Function
---------------------------------------------------------------

Overview:
---------
- Evaluates a polynomial using Newton's divided difference formula.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): Coefficients of the polynomial.
- c (list): Nodes of the polynomial.
- z (number): The point at which to evaluate the polynomial.

Returns:
--------
- number: The value of the polynomial at point z.
- Raises TypeError for non-list inputs.
- Raises ValueError for empty lists or lists of different lengths.

Functionality:
--------------
- Newton's Method: Efficiently computes the value of a polynomial at a given point using divided differences.

Example Usage:
--------------
> coefficients = [1, 2, 3]
> nodes = [0, 1, 2]
> x = 1.5
> result = evaluateNewton(coefficients, nodes, x)
> print(result)  # Output: 4.0

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for empty lists or lists of different lengths.

Test Suite:
-----------
- Tests include polynomial evaluation, handling empty lists, mismatched list lengths, and invalid input types.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
