import sys
import unittest
import random

# Adjust the path as necessary to import my_utils
sys.path.append('../../src/')

import my_utils


class TestMyUtils(unittest.TestCase):
    """
    Unit tests for my_utils.py functions: mean, median, std_dev.
    """
    def test_mean(self):
        self.assertEqual(my_utils.mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(my_utils.mean([]), None)
        self.assertEqual(my_utils.mean([10]), 10.0)
        self.assertAlmostEqual(my_utils.mean([1.5, 2.5, 3.5]), 2.5)
        self.assertRaises(TypeError, my_utils.mean, [1, 'a', 3])
        random.seed(42)
        data = [random.randint(1, 100) for i in range(10)]
        expected_mean = sum(data) / len(data)
        self.assertEqual(my_utils.mean(data), expected_mean)
        self.assertFalse(my_utils.mean([1.5, 2.5, 3.5]) == 0)
        self.assertTrue(my_utils.mean([1, 2, 3, 4, 5]) != 4.0)

    def test_median(self):
        self.assertEqual(my_utils.median([1, 3, 3, 6, 7, 8, 9]), 6.0)
        self.assertEqual(my_utils.median([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertEqual(my_utils.median([]), None)
        self.assertEqual(my_utils.median([10]), 10.0)
        self.assertEqual(my_utils.median([1.5, 2.5, 3.5]), 2.5)
        self.assertRaises(TypeError, my_utils.median, [2, 'b', 5])
        self.assertFalse(my_utils.median([1, 3, 3, 6, 7, 8, 9]) == 5.0)
        self.assertTrue(my_utils.median([1, 2, 3, 4, 5, 6]) != 4.0)
        random.seed(42)
        data = [random.randint(1, 100) for i in range(11)]
        sorted_data = sorted(data)
        expected_median = sorted_data[len(sorted_data) // 2]
        self.assertEqual(my_utils.median(data), expected_median)

    def test_std_dev(self):
        self.assertAlmostEqual(my_utils.std_dev(
                                [10, 12, 23, 23, 16, 23, 21, 16]),
                               4.898979485566356)
        self.assertEqual(my_utils.std_dev([]), None)
        self.assertEqual(my_utils.std_dev([10]), 0.0)
        self.assertAlmostEqual(my_utils.std_dev([1.5, 2.5, 3.5]),
                               0.816496580927726)
        self.assertRaises(TypeError, my_utils.std_dev, [1, 'c', 3])
        self.assertFalse(my_utils.std_dev(
                        [10, 12, 23, 23, 16, 23, 21, 16]) == 5.0)
        self.assertTrue(my_utils.std_dev([1.5, 2.5, 3.5]) != 1.0)
        random.seed(42)
        data = [random.randint(1, 100) for i in range(10)]
        mean_value = sum(data) / len(data)
        variance = sum((x - mean_value) ** 2 for x in data) / len(data)
        expected_std_dev = variance ** 0.5
        self.assertAlmostEqual(my_utils.std_dev(data), expected_std_dev)


if __name__ == '__main__':
    unittest.main()
