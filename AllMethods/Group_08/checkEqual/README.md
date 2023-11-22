---------------------------------------------------------------
        checkEqual Function
---------------------------------------------------------------

Overview:
---------
- Compares two lists or tuples for element-wise equality.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- a (list or tuple): The first list or tuple to compare.
- b (list or tuple): The second list or tuple to compare.

Returns:
--------
- bool: Returns True if both lists/tuples are equal, False otherwise.
- Raises TypeError for non-list or non-tuple inputs.

Functionality:
--------------
- Input Validation: Checks if both inputs are lists or tuples.
- Length Check: Returns False if lengths of inputs differ.
- Element-wise Comparison: Iterates through the inputs and compares each element.

Example Usage:
--------------
> list1 = [1, 2, 3]
> list2 = [1, 2, 3]
> result = check_equal(list1, list2)
> print(result)  # Output: True

Error Handling:
---------------
- TypeError: Raised if inputs are not lists or tuples.

Test Suite:
-----------
- Tests include equal lists, unequal lists, different lengths, non-list inputs, equal tuples, and unequal tuples.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
