import unittest

from daily.d7_sort_list.solution import sort_nums


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 1, 2, 2, 3, 3, 3], sort_nums([3, 3, 2, 1, 3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
