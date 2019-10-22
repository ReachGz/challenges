import unittest

from hackerrank.new_year_chaos.solution import minimum_bribes


class MyTestCase(unittest.TestCase):
    def test_1(self):
        r = minimum_bribes([2, 1, 5, 3, 4])
        self.assertEqual(3, r)

    def test_2(self):
        r = minimum_bribes([2, 5, 1, 3, 4])
        self.assertEqual('Too chaotic', r)

    def test_3(self):
        # 1 2 3 4 5
        # 1 3 2 4 5 -- 3 -> 2
        # 3 1 2 4 5 -- 3 -> 1
        # 3 2 1 4 5 -- 2 -> 1
        r = minimum_bribes([3, 2, 1, 4, 5])
        self.assertEqual(3, r)

    def test_4(self):
        r = minimum_bribes([5, 1, 2, 3, 7, 8, 6, 4])
        self.assertEqual('Too chaotic', r)

    def test_5(self):
        r = minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])
        self.assertEqual(7, r)

    def test_6(self):
        r = minimum_bribes([1, 2, 5, 3, 4, 7, 8, 6])
        self.assertEqual(4, r)

    # def test_7(self):
    #     r = minimum_bribes(list(range(1, 100000)))
    #     self.assertEqual(0, r)


if __name__ == '__main__':
    unittest.main()
