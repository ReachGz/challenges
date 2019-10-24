import unittest

from daily.d5_indices_in_sorted_array.solution import get_range


class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
        target = 2
        self.assertEqual([1, 4], get_range(arr, target))

    def test_2(self):
        arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
        target = 9
        self.assertEqual([6, 8], get_range(arr, target))

    def test_3(self):
        arr = [100, 150, 150, 153]
        target = 150
        self.assertEqual([1, 2], get_range(arr, target))

    def test_4(self):
        arr = [1, 2, 3, 4, 5, 6, 10]
        target = 9
        self.assertEqual([-1, -1], get_range(arr, target))

    def test_5(self):
        arr = [1, 2, 3, 4, 5, 9, 10]
        target = 9
        self.assertEqual([5, 5], get_range(arr, target))


if __name__ == '__main__':
    unittest.main()
