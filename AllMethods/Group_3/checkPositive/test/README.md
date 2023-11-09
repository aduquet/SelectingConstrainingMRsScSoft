
# Testing `checkPositive` Function

This repository contains tests for the `checkPositive` function, which checks if all elements in a list are positive numbers.

## Tests Explanation:

- `test_all_positive`: Tests a list containing all positive numbers.
- `test_contains_negative`: Tests a list containing a negative number.
- `test_empty_list`: Tests an empty list.
- `test_invalid_elements`: Checks for a `ValueError` when the list contains non-numeric elements.
- `test_invalid_input_type`: Checks for a `TypeError` when the input is not a list.

## Running the Tests:

1. **Using unittest from Command Line**:
   ```bash
   python -m unittest test_checkPositive.py
   ```

2. **Running the Script Directly**:
   ```bash
   python test_checkPositive.py
   ```

For a more detailed output, add `-v` to the command:
   ```bash
   python -m unittest -v test_checkPositive.py
   ```