

## sequential_search Function

### Overview
The `sequential_search` function implements a linear search algorithm to find a specified key within a list.

### Requirements
- Python 3.x

### Parameters
- `a` (list): The list in which to search.
- `key`: The value being searched for in the list.

### Returns
- Returns the index of the `key` in the list if it's found; otherwise, returns `None`.

### Functionality
- Iteratively checks each element in the list against the `key`.
- If a match is found, it returns the index of that element.
- If no match is found by the end of the list, returns `None`.

### Example Usage
```python
data = [5, 3, 7, 1, 4]
key_to_find = 7
result = sequential_search(data, key_to_find)
print("Index:", result)  # Output: Index: 2
```

### Error Handling
- This function does not raise errors. If the `key` is not in the list, the function simply returns `None`.

### Test Suite
- Includes tests for both successful and unsuccessful searches.
- Ensures the function correctly identifies the index of the `key` or returns `None` as appropriate.

### Running Tests
- Utilizes Python's `unittest` framework.
- Combine the function and test suite into a single script for testing.
- Execute the script to run tests and display results.

---

This README is formatted for readability and clarity on GitHub, providing comprehensive information about the `sequential_search` function's purpose, usage, and testing.