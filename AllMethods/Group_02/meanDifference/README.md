---------------------------------------------------------------
    meanDifference Function
---------------------------------------------------------------

Overview:
---------
- Calculates the mean of the differences between elements of two samples.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- sample1 (list): The first sample of numbers.
- sample2 (list): The second sample of numbers.

Returns:
--------
- float: The mean difference between the two samples.
- Raises TypeError for non-list inputs.
- Raises ValueError for samples of different lengths or empty samples.

Functionality:
--------------
- Input Validation: Ensures both inputs are lists, of the same length, and not empty.
- Mean Difference Calculation: Computes the average of the differences between corresponding elements of the two samples.

Example Usage:
--------------
> sample1 = [1, 2, 3]
> sample2 = [4, 5, 6]
> result = meanDifference(sample1, sample2)
> print(result)  # Output: -3

Error Handling:
---------------
- TypeError: Raised for non-list inputs.
- ValueError: Raised for samples of different lengths or empty samples.

Test Suite:
-----------
- Tests include mean difference calculation, mismatched sample lengths, empty samples, and invalid input types.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
