### README for `weightedMean` Function

#### Overview

The `weightedMean` function calculates the weighted mean of a set of elements, each having a corresponding weight. It's a measure of central tendency that considers the importance of each value.

#### Function Signature

```python
def weightedMean(elements, theWeights):
    # function implementation
```

#### Parameters

- `elements` (list): The list of numerical values.
- `theWeights` (list): The list of weights corresponding to each element in `elements`.

#### Returns

- `float`: The weighted mean of the elements.

#### Process

1. Validates that `elements` and `theWeights` have the same length.
2. Calculates the total weighted sum and the sum of weights.
3. Computes the weighted mean.

#### Test Suite

A test suite is provided to ensure correct handling of normal cases, different weights, zero weights, and mismatched lengths.

#### Notes

- The function ensures that the sum of weights is not zero to prevent division by zero.
- `elements` and `theWeights` must be of the same length.

#### Example Usage

```python
elements = [10, 20, 30, 40, 50]
weights = [1, 2, 3, 4, 5]
weighted_mean = weightedMean(elements, weights)
```

This calculates the weighted mean of `elements` using `weights`.

