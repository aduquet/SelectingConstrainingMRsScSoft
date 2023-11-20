import unittest

class TestEvaluateNewton(unittest.TestCase):
    def test_evaluate_newton(self):
        self.assertAlmostEqual(evaluateNewton([1, 2, 3], [0, 1, 2], 1.5), 4.0)

    def test_empty_lists(self):
        with self.assertRaises(ValueError):
            evaluateNewton([], [], 1)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            evaluateNewton([1, 2], [1, 2, 3], 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            evaluateNewton("not a list", [1, 2, 3], 1)

if __name__ == "__main__":
    unittest.main()
