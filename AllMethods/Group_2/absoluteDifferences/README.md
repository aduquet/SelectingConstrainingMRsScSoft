---------------------------------------------------------------
    absoluteDifferences Function
---------------------------------------------------------------

Overview:
---------
- Calculates the absolute values of elements in a list.
- Handles mixed data types in the list.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- z (list): A list of numbers (integers or floats).

Returns:
--------
- list: A new list with the absolute values of numeric elements in z.
- Raises TypeError if the input is not a list.

Functionality:
--------------
- Type Checking: Verifies that input is a list.
- Calculation: Converts each numeric element to its absolute value.
- Non-Numeric Handling: Returns None for non-numeric elements.

Example Usage:
--------------
> data = [-3, 4, 'a', 0]
> result = absoluteDifferences(data)
> print(result)  # Output: [3, 4, None, 0]

Test Suite:
-----------
- Includes tests for mixed data, empty list, non-list input, and all positive values.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
