---------------------------------------------------------------
    meanDeviation Function
---------------------------------------------------------------

Overview:
---------
- Calculates the mean absolute deviation of a set of elements from their mean.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- elements (list): A list of numerical elements.
- mean (number): The mean value of the elements.

Returns:
--------
- float: The mean absolute deviation.
- Raises TypeError for non-list elements input.
- Raises ValueError if the elements list is empty.

Functionality:
--------------
- Input Validation: Ensures that elements is a list and is not empty.
- Deviation Calculation: Computes the average of the absolute differences between each element and the mean.

Example Usage:
--------------
> data = [1, 2, 3, 4, 5]
> mean_value = 3
> result = meanDeviation(data, mean_value)
> print(result)  # Output: 1.2

Error Handling:
---------------
- TypeError: Raised for non-list elements input.
- ValueError: Raised if the elements list is empty.

Test Suite:
-----------
- Tests include mean deviation calculation, handling of empty list, and invalid input type.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
