---------------------------------------------------------------
    errorRate Function
---------------------------------------------------------------

Overview:
---------
- Calculates the error rate based on provided labels and predictions.

Requirements:
-------------
- Python 3.x

Parameters:
-----------
- labels (list or tuple): The list of actual labels.
- predictions (list or tuple): The list of predicted labels.

Returns:
--------
- float: The error rate calculated as the number of mismatches divided by the number of comparisons.
- Raises TypeError for non-list/tuple inputs.
- Raises ValueError for lists of different lengths or all invalid predictions.

Functionality:
--------------
- Input Validation: Ensures both labels and predictions are lists or tuples of the same length.
- Error Rate Calculation: Compares labels and predictions to calculate the error rate.

Example Usage:
--------------
> labels = [1, 2, 3, 4]
> predictions = [1, 2, 4, 3]
> result = errorRate(labels, predictions)
> print(result)  # Output: 0.5

Error Handling:
---------------
- TypeError: Raised for non-list/tuple inputs.
- ValueError: Raised for lists of different lengths or all invalid predictions.

Test Suite:
-----------
- Tests include error rate calculation, all invalid predictions, mismatched list lengths, and invalid input types.
- Validates the function's correctness and error handling.

Running Tests:
--------------
- Use the unittest framework in Python.
- Combine the function and test suite in one script.
- Run the script to execute tests and view results.

---------------------------------------------------------------
