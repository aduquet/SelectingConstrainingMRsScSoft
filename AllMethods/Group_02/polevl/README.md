---------------------------------------------------------------
    pooledMean Function
---------------------------------------------------------------

Overview:
---------
- Calculates the pooled mean of two data sets.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- data1 (list): The first data set.
- data2 (list): The second data set.

Returns:
--------
- float: The pooled mean of the two data sets.
- Raises ValueError if either of the data sets is empty.

Functionality:
--------------
- Input Validation: Ensures neither of the data sets is empty.
- Pooled Mean Calculation: Computes a weighted average of the means of both data sets.

Example Usage:
--------------
> data_set1 = [1, 2, 3]
> data_set2 = [4, 5, 6, 7]
> result = pooledMean(data_set1, data_set2)
> print(result)  # Output: 4

Error Handling:
---------------
- ValueError: Raised if either of the data sets is empty.

Test Suite:
-----------
- Tests include pooled mean calculation and handling of empty data sets.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
