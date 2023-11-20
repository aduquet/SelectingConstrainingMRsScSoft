
### README for `chebyshevDistance` Function

#### Overview
The `chebyshevDistance` function calculates the Chebyshev distance between two points. The Chebyshev distance, also known as the maximum metric, is a metric defined on a vector space where the distance between two vectors is the greatest of their differences along any coordinate dimension.

#### Function Signature
```python
def chebyshevDistance(p1, p2):
    # function implementation
```

#### Parameters
- `p1` (list): The first point in n-dimensional space.
- `p2` (list): The second point in n-dimensional space.

#### Returns
- `float`: The Chebyshev distance between `p1` and `p2`.

#### Process
1. Validates that both `p1` and `p2` are lists.
2. Checks that `p1` and `p2` have the same length.
3. Calculates the Chebyshev distance by finding the maximum absolute difference between corresponding elements of `p1` and `p2`.

#### Test Suite
A test suite for this function would include tests for typical scenarios such as valid inputs with varying dimensions, as well as edge cases like type mismatches and differing lengths.

#### Example Usage
```python
distance = chebyshevDistance([1, 2, 3], [4, 2, 1])
# distance will be 3
```
This example calculates the Chebyshev distance between two points in a 3-dimensional space.

#### Notes
- The Chebyshev distance is particularly useful in chess, warehouse logistics, and various other fields where a grid-like metric is used.