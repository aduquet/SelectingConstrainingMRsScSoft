
# README for `add_two_array_values` Function

## Overview

The `add_two_array_values` function is a Python function designed to perform a specific operation on a list or tuple. It takes three parameters: a list or tuple `a`, and two integer indices `i` and `j`. The function adds the value at index `i` to half the value at index `j` in the given list or tuple.

## Function Signature

```python
def add_two_array_values(a, i, j):
```

## Parameters

- `a` (list or tuple): The list or tuple on which the operation is to be performed.
- `i` (int): The index of the first element in `a`.
- `j` (int): The index of the second element in `a`.

## Returns

- `float` or `int`: The result of adding the value at index `i` to half the value at index `j` in `a`.

## Exceptions

- `TypeError`: Raised if `a` is not a list or tuple, or if either `i` or `j` is not an integer.
- `IndexError`: Raised if either `i` or `j` is out of bounds for the list or tuple `a`.

## Usage Example

```python
array = [10, 20, 30, 40]
result = add_two_array_values(array, 1, 2)
print(result)  # Output will be 35.0
```

In this example, the function will add the value at index `1` (which is 20) to half the value at index `2` (which is 15), resulting in 35.0.

## Notes

- The function expects `i` and `j` to be valid indices for the list or tuple `a`. If either index is out of the valid range, an `IndexError` is raised.
- The function handles both lists and tuples, but it does not support other iterable types.
- The return type depends on the types of elements in `a`. If the elements are integers, the return type will be `float`, since the division operation converts the result to a float.
- The function performs a division by 2, which is a floating-point division in Python 3. Hence, even if the elements of `a` are integers, the returned value could be a float.

## Tests

A series of tests are provided to ensure the function behaves as expected. These tests check for valid indices, handle invalid indices, verify the type of input, and ensure the indices are integers.

### Test Cases

- `test_valid_indices`: Confirms that the function returns the correct result for valid input.
- `test_invalid_indices`: Expects an `IndexError` when indices are out of bounds.
- `test_invalid_array`: Expects a `TypeError` when the first argument is not a list or tuple.
- `test_non_integer_indices`: Expects a `TypeError` when indices are not integers.