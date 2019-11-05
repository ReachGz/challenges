import unittest

from daily.d10_non_decreasing.solution import non_decreasing


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertTrue(non_decreasing([13, 4, 7]))

    def test_2(self):
        self.assertFalse(non_decreasing([5, 1, 3, 2, 5]))


if __name__ == '__main__':
    unittest.main()
