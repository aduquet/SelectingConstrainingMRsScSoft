
### README

Here's a basic README for the function:

```
# Array Value Retrieval Function

## Description
This Python function `get_array_value` retrieves an element from an array based on a 1-based index. If the index is out of the array's bounds, it returns `None`.

## Usage
```python
result = get_array_value(array, index)
```

- `array`: The array from which you want to retrieve the value.
- `index`: The 1-based index of the element you want to retrieve.

## Example
```python
array = [1, 2, 3, 4, 5]
print(get_array_value(array, 3)) # Outputs: 3
```

## Testing
A simple test suite is included to validate the functionality of `get_array_value`. It checks for basic usage, boundary conditions, and error handling.
```
