
### sampleKurtosis

The `sampleKurtosis` function you've provided calculates the sample kurtosis of a dataset. Kurtosis is a measure of the "tailedness" of the probability distribution of a real-valued random variable. In simpler terms, it measures how heavy or light the tails of the distribution are compared to a normal distribution.

### Function Signature

```python
def sampleKurtosis(size, moment4, sampleVariance):
    # function body
```

- `size` (int): The size of the sample, often denoted as \( n \) in statistical formulas.
- `moment4` (float): The fourth central moment of the dataset.
- `sampleVariance` (float): The variance of the sample.

### Calculation Process

1. The function calculates the fourth moment standardized by the square of the variance.
2. It multiplies this standardized moment by a scaling factor related to the sample size.
3. It subtracts another factor to adjust for the bias in a sample as opposed to the entire population.

### Return Value

- The function returns the sample kurtosis, a measure of the tailedness of the distribution.

### Formula

The sample kurtosis is computed using the formula:

\[
\text{Sample Kurtosis} = \frac{m4 \cdot n \cdot (n + 1)}{(n - 1) \cdot (n - 2) \cdot (n - 3) \cdot s2^2} - 3 \cdot \frac{(n - 1)^2}{(n - 2) \cdot (n - 3)}
\]

where \( m4 \) is the fourth central moment, \( n \) is the sample size, and \( s2 \) is the sample variance.

### Important Notes

- The function assumes that the input parameters are correct and doesn't perform any validation.
- Sample kurtosis can be sensitive to the sample size. Small samples might not give a reliable estimate.
- The function is designed to be used with a reasonable sample size (usually \( n > 3 \)) to avoid division by zero or negative numbers in the denominator.

### Example Usage

```python
size = 100
moment4 = calculate_moment4(data)
sampleVariance = calculate_sample_variance(data)

kurtosis = sampleKurtosis(size, moment4, sampleVariance)
```
