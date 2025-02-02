import unittest
import numpy as np
from plot_population import calculate_mean, calculate_confidence_intervals

class TestPopulationFunctions(unittest.TestCase):

    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        result = calculate_mean(data)
        self.assertEqual(result, 3.0)

    def test_calculate_confidence_intervals(self):
        std_devs = [10, 20, 30]
        sample_size = 10
        expected_intervals = [1.96 * (std / np.sqrt(sample_size)) for std in std_devs]
        result = calculate_confidence_intervals(std_devs, sample_size)
        self.assertEqual(result, expected_intervals)

if __name__ == '__main__':
    unittest.main()
