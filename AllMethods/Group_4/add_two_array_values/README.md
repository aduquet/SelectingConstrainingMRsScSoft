# Program Description

This program includes a function `add_two_array_values(a, i, j)` which takes a list `a` and two integer indices `i` and `j`. The function returns the sum of the element at index `i` and half the value of the element at index `j`.

## Tests

A series of tests are provided to ensure the function behaves as expected. These tests check for valid indices, handle invalid indices, verify the type of input, and ensure the indices are integers.

### Test Cases

- `test_valid_indices`: Confirms that the function returns the correct result for valid input.
- `test_invalid_indices`: Expects an `IndexError` when indices are out of bounds.
- `test_invalid_array`: Expects a `TypeError` when the first argument is not a list or tuple.
- `test_non_integer_indices`: Expects a `TypeError` when indices are not integers.