import unittest

from daily.d3_longest_palindromic_substring.solution import longest_palindrome


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual('racecar', longest_palindrome('tracecars'))

    def test_2(self):
        self.assertEqual('anana', longest_palindrome('banana'))

    def test_3(self):
        self.assertEqual('illi', longest_palindrome('million'))

    def test_4(self):
        self.assertEqual(None, longest_palindrome('abcdefg'))


if __name__ == '__main__':
    unittest.main()
