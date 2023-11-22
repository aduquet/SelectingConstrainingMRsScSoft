---------------------------------------------------------------
    evaluateHorner Function
---------------------------------------------------------------

Overview:
---------
- Evaluates a polynomial at a given point using Horner's method.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- coefficients (list): List of coefficients of the polynomial.
- argument (number): The point at which to evaluate the polynomial.

Returns:
--------
- number: The value of the polynomial at the given point.
- Raises ValueError if the coefficient list is empty.

Functionality:
--------------
- Horner's Method: Efficiently computes the value of a polynomial at a given point.

Example Usage:
--------------
> coefficients = [1, 2, 3]
> x = 2
> result = evaluateHorner(coefficients, x)
> print(result)  # Output: 11

Error Handling:
---------------
- ValueError: Raised if the coefficient list is empty.

Test Suite:
-----------
- Tests include evaluating a polynomial and handling an empty coefficient list.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
