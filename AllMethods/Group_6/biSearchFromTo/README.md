---------------------------------------------------------------
          biSearchFromTo Function
---------------------------------------------------------------

Overview:
---------
- Implements binary search within a specified range of an array.
- Efficient for locating a target value in a sorted array.

Requirements:
-------------
- Python Version: Python 3.x

Parameters:
-----------
- arr (list of int): Sorted list of integers for the search.
- target (int): Target value to search for.
- start (int): Starting index of the search range.
- end (int): Ending index of the search range.

Returns:
--------
- int: Index of the target if found, otherwise negative insertion point.

Functionality:
--------------
- Repeatedly divides the search interval in half.
- Narrows down to either the lower or upper half based on comparison.
- Continues until the target is found or interval is empty.

Example Usage:
--------------
> test_array = [1, 3, 5, 7, 9]
> target_value = 5
> start_index = 0
> end_index = 4
> result = binary_search_from_to(test_array, target_value, start_index, end_index)
> print(result)  # Output: 2

Test Suite:
-----------
- Ensures correct functionality through various test cases.
- Includes tests for found target, nonexistent target, empty array, and single element array.

Running Tests:
--------------
- Use the unittest framework in Python.
- Include both the function and test suite in the script.
- Execute the script to run and view test results.

---------------------------------------------------------------
