---------------------------------------------------------------
    power Function
---------------------------------------------------------------

Overview:
---------
- Raises each element in a list to a specified power.

Requirements:
-------------
- Python 3.x
- math module

Parameters:
-----------
- data (list): A list of numerical values.
- k (number): The power to which each element is raised.

Returns:
--------
- list: A list where each element is raised to the power k.
- Raises TypeError if input is not a list.

Functionality:
--------------
- List Processing: Iterates through the list, raising each element to the power k.
- Option for In-Place Modification: The original list can be modified in place, or a new list can be returned.

Example Usage:
--------------
> data = [2, 3, 4]
> exponent = 2
> result = power(data, exponent)
> print(result)  # Output: [4, 9, 16]

Error Handling:
---------------
- TypeError: Raised if the input is not a list.

Test Suite:
-----------
- Tests include power raising for a list of numbers, handling of an empty list, and invalid input type.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
