
# Testing `checkNonNegative` Function

This repository contains tests for the `checkNonNegative` function, which checks if all elements in a list are non-negative.

## Tests Explanation:

- `test_empty_list`: Tests an empty list (should return `True` since there are no negative numbers).
- `test_all_positive_numbers`: Tests a list containing only positive numbers.
- `test_negative_numbers`: Tests a list that contains negative numbers.
- `test_invalid_non_numeric_element`: Checks for a `ValueError` when the list contains non-numeric elements.
- `test_invalid_input_type`: Checks for a `TypeError` when the input is not a list.

## Running the Tests:

1. **Using unittest from Command Line**:
   ```bash
   python -m unittest test_checkNonNegative.py
   ```

2. **Running the Script Directly**:
   ```bash
   python test_checkNonNegative.py
   ```

For a more detailed output, add `-v` to the command:
   ```bash
   python -m unittest -v test_checkNonNegative.py
   ```
