import unittest

from hackerrank.array_manipulation.solution import array_manipulation


class MyTestCase(unittest.TestCase):
    def test_1(self):
        r = array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]])
        self.assertEqual(200, r)


if __name__ == '__main__':
    unittest.main()
