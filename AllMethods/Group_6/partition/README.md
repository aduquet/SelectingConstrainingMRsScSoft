# autoCorrelation Function

The `autoCorrelation` function calculates the autocorrelation of a given data series with a specified lag, mean, and variance. Autocorrelation measures the similarity between a data point and a data point at a certain time lag.

## Function Implementation

The function computes autocorrelation using the formula:

`ACF(lag) = Σ[(X(t) - mean) * (X(t - lag) - mean)] / [(N - lag) * variance]`


Where:
- `data` is the input data series.
- `lag` is the time lag for which autocorrelation is computed.
- `mean` is the mean of the data series.
- `variance` is the variance of the data series.

## Test Suite

A test suite using the `unittest` framework is provided to verify the correctness of the `autoCorrelation` function. The test case `test_auto_correlation` checks if the function correctly calculates the autocorrelation for a sample data series.

## Running the Tests

To run the tests, execute the following command:

```bash
python test_auto_correlation.py
