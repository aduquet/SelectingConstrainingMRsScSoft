---------------------------------------------------------------
                  array_calc1 Function
---------------------------------------------------------------

Overview:
---------
The `array_calc1` function performs element-wise division of an array by an integer.
It takes two parameters: an array (r0) and an integer divisor (i0), and returns a
new array with the division results.

Requirements:
-------------
- Python Version: Python 3.x

Parameters:
-----------
- r0 (list): An array of numbers (integers or floats).
- i0 (int): An integer divisor.

Returns:
--------
- list: A new list with each element in r0 divided by i0.

Functionality:
--------------
1. Input Validation:
   - Checks for zero division. Raises ValueError if i0 is 0.
   - Validates input types. Raises TypeError if r0 is not a list or i0 is not an integer.

2. Division Operation:
   - Initializes a new list r1 with the same length as r0.
   - Divides each element in r0 by i0 and stores the result in r1.

Example Usage:
--------------
> array = [10, 20, 30, 40]
> divisor = 10
> result = array_calc1(array, divisor)
> print(result)
[1.0, 2.0, 3.0, 4.0]

Error Handling:
---------------
- Division by Zero: Raises ValueError with "Division by zero is not allowed."
- Invalid Input Types: Raises TypeError with "Invalid input types."

Notes:
------
- Suitable for numerical operations only.
- Python division results in float values, even for integer elements in r0.

---------------------------------------------------------------
