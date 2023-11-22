---------------------------------------------------------------
    scale Function
---------------------------------------------------------------

Overview:
---------
- Scales each element in a list by a specified factor.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- val (number): The scaling factor.
- arr (list): The list of numbers to be scaled.

Returns:
--------
- list: A new list where each element is scaled by 'val'.

Functionality:
--------------
- List Scaling: Multiplies each element in the input list by the scaling factor.

Example Usage:
--------------
> scaling_factor = 2
> original_list = [1, 2, 3]
> scaled_list = scale(scaling_factor, original_list)
> print(scaled_list)  # Output: [2, 4, 6]

Error Handling:
---------------
- Handles empty lists by returning an empty list.

Test Suite:
-----------
- Tests include scaling a list of numbers and handling an empty list.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
