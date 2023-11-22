---------------------------------------------------------------
    count_k Function
---------------------------------------------------------------

Overview:
---------
- Counts the occurrences of a value 'k' in a list or tuple 'a'.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list or tuple): The list or tuple in which to count occurrences.
- k (any type): The value to count.

Returns:
--------
- int: The number of occurrences of 'k' in 'a'.
- Raises TypeError if 'a' is not a list or tuple.

Functionality:
--------------
- Input Validation: Ensures 'a' is a list or tuple.
- Counting: Iterates through 'a' and counts occurrences of 'k'.

Example Usage:
--------------
> data = [1, 2, 3, 2, 4, 2]
> key = 2
> result = count_k(data, key)
> print(result)  # Output: 3

Error Handling:
---------------
- TypeError: Raised if 'a' is not a list or tuple.

Test Suite:
-----------
- Tests include counting occurrences, no occurrences, and invalid input type.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
