---------------------------------------------------------------
        clip Function
---------------------------------------------------------------

Overview:
---------
- Clips the elements of a list within specified lower and upper limits.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list): The list to be clipped.
- lowerLim (number): The lower boundary for clipping.
- upperLim (number): The upper boundary for clipping.

Returns:
--------
- list: A new list with the clipped elements.

Functionality:
--------------
- Iterates over the list and clips each element to be within the given limits.

Example Usage:
--------------
> data = [1, 2, 3, 4, 5]
> lower_limit = 2
> upper_limit = 4
> result = clip(data, lower_limit, upper_limit)
> print(result)  # Output: [2, 2, 3, 4, 4]

Test Suite:
-----------
- Includes tests for normal usage, empty lists, no clipping needed, and all elements clipped.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
