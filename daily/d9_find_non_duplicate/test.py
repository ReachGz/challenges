import unittest

from daily.d9_find_non_duplicate.solution import single_number


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, single_number([4, 3, 2, 4, 1, 3, 2]))


if __name__ == '__main__':
    unittest.main()
