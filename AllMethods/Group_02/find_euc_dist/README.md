
### README for `find_euc_dist` Function

#### Overview

The `find_euc_dist` function calculates the Euclidean distance between two points in n-dimensional space, where the points are represented as lists of coordinates.

#### Function Signature

```python
def find_euc_dist(a, b):
    # function implementation
```

#### Parameters

- `a` (list): The first point in n-dimensional space.
- `b` (list): The second point in n-dimensional space.

#### Returns

- `float`: The Euclidean distance between `a` and `b`.

#### Process

1. Validates that `a` and `b` have the same length.
2. Calculates the sum of squared differences between corresponding elements of `a` and `b`.
3. Returns the square root of this sum.

#### Test Suite

A test suite for this function includes tests for valid distances, zero distance, and mismatched list lengths.

#### Example Usage

```python
distance = find_euc_dist([1, 2, 3], [4, 5, 6])
# distance will be approximately 5.196
```

This example calculates the Euclidean distance between two points in a 3-dimensional space.

#### Notes

- The function expects `a` and `b` to be of the same length and contain numeric values.
- The Euclidean distance is the "ordinary" distance between two points, which can be visualized as the length of a straight line connecting them.