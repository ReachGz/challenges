import unittest

from daily.d2_longest_substring.solution import longest_substring_length


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(10, longest_substring_length('abrkaabcdefghijjxxx'))

    def test_2(self):
        self.assertEqual(1, longest_substring_length('a'))

    def test_3(self):
        self.assertEqual(12, longest_substring_length('abcdefghijkl'))

    def test_3(self):
        self.assertEqual(12, longest_substring_length('abcabcdefghijkl'))

    def test_3(self):
        self.assertEqual(12, longest_substring_length('abcabcdefghijklabc'))


if __name__ == '__main__':
    unittest.main()
