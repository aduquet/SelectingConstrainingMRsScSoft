
### README for `weightedRMS` Function

#### Overview

The `weightedRMS` function calculates the weighted root mean square of a dataset with corresponding weights. It's a measure that combines the magnitude of the numbers with their importance (weights).

#### Function Signature

```python
def weightedRMS(data, weights):
    # function implementation
```

#### Parameters

- `data` (list): The list of numerical values.
- `weights` (list): The list of weights corresponding to each element in `data`.

#### Returns

- `float`: The weighted RMS of the data.

#### Process

1. Validates that `data` and `weights` have the same length and that the sum of weights is not zero.
2. Calculates the sum of squared products and the sum of weights.
3. Computes the weighted RMS.

#### Test Suite

The test suite ensures the function handles normal cases, different weights, zero weights, and mismatched lengths correctly.

#### Notes

- Both `data` and `weights` should be of the same length.
- The sum of weights should not be zero to avoid division by zero.

#### Example Usage

```python
data = [10, 20, 30, 40, 50]
weights = [1, 2, 3, 4, 5]
weighted_rms = weightedRMS(data, weights)
```

This calculates the weighted RMS of `data` using `weights`.

