import unittest

def lag1_autocorrelation(elements, mean):
    v = (elements[0] - mean) ** 2
    q = 0
    for i in range(len(elements)):
        delta0 = elements[i - 1] - mean if i > 0 else 0
        delta1 = elements[i] - mean

        q = q + (delta0 * delta1 - q) / (i + 1)
        v = v + (delta1 ** 2 - v) / (i + 1)

    return q / v if v != 0 else 0

class TestLag1Autocorrelation(unittest.TestCase):

    def test_normal_data(self):
        data = [1, 2, 3, 4, 5]
        mean_data = sum(data) / len(data)
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 1)

    def test_constant_data(self):
        data = [1, 1, 1, 1]
        mean_data = sum(data) / len(data)
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 0)

    def test_empty_data(self):
        data = []
        mean_data = 0
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 0)

    def test_single_element_data(self):
        data = [5]
        mean_data = sum(data) / len(data)
        result = lag1_autocorrelation(data, mean_data)
        self.assertEqual(result, 0)

# This allows the test cases to be run from the command line
if __name__ == '__main__':
    unittest.main()
