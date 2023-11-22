
#### Overview `sampleSkew` Function

The `sampleSkew` function is a Python function designed to calculate the sample skewness of a given set of data. Skewness measures the asymmetry of the probability distribution of a real-valued random variable.

#### Function Signature

```python
def sampleSkew(size, moment3, sampleVariance):
    # function implementation
```

#### Parameters

- `size` (int): The size of the sample.
- `moment3` (float): The third central moment of the dataset.
- `sampleVariance` (float): The variance of the sample.

#### Returns

- `float`: The calculated sample skewness for the given data.

#### Process

1. Validates the input parameters for sample size and variance.
2. Calculates the skewness using the formula that involves the third central moment and the square root of the variance.

#### Test Suite

A test suite is provided to ensure the function's correctness under various scenarios, including normal cases and edge cases like small sample sizes or negative variances.

#### Notes

- The function assumes the inputs are correctly provided. It includes checks for sample size and variance positivity.
- Skewness can be sensitive to the sample size. Small samples might not provide a reliable estimate.

#### Example Usage

```python
size = 100
moment3 = calculate_moment3(data)
sampleVariance = calculate_sample_variance(data)

skewness = sampleSkew(size, moment3, sampleVariance)
```

In this example, you need to calculate the third central moment and the sample variance of your data set before using the `sampleSkew` function.
