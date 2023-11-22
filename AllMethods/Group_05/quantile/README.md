---------------------------------------------------------------
    quantile Function
---------------------------------------------------------------

Overview:
---------
- Calculates the quantile of a sorted list of elements.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- sortedElements (list): A sorted list of numerical elements.
- phi (float): The quantile to compute, ranging from 0 to 1.

Returns:
--------
- float: The computed quantile value.
- Raises ValueError for an empty list or an invalid phi value.

Functionality:
--------------
- Quantile Calculation: Computes a quantile value by interpolating between ranks in the sorted list.

Example Usage:
--------------
> elements = [1, 2, 3, 4, 5]
> phi = 0.5
> result = quantile(elements, phi)
> print(result)  # Output: 3

Error Handling:
---------------
- ValueError: Raised if the list is empty or if phi is not in the range [0, 1].

Test Suite:
-----------
- Tests include quantile calculation at various points, handling of empty list, and invalid phi values.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
