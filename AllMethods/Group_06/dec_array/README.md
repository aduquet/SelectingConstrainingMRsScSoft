---------------------------------------------------------------
    dec_array Function
---------------------------------------------------------------

Overview:
---------
- Decreases each element in an array by a specified amount.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The list of numbers to be decremented.
- k (int or float): The decrement value.

Returns:
--------
- list: A new list with each element decremented by k.
- Raises TypeError if inputs are of incorrect types.

Functionality:
--------------
- Input Validation: Ensures 'a' is a list and 'k' is a number.
- Decrement: Reduces each element in 'a' by 'k'.

Example Usage:
--------------
> data = [1, 2, 3, 4]
> decrement_value = 2
> result = dec_array(data, decrement_value)
> print(result)  # Output: [-1, 0, 1, 2]

Error Handling:
---------------
- TypeError: Raised for incorrect input types.

Test Suite:
-----------
- Tests include decrementing an array, invalid list input, and invalid decrement value.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
