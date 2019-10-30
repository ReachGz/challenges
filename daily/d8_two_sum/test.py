import unittest

from daily.d8_two_sum.solution import two_sum


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, two_sum([4, 7, 1, -3, 2], 5))


if __name__ == '__main__':
    unittest.main()
