import unittest

from daily.d4_balanced_parentheses.solution import is_balanced


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, is_balanced('((()))'))

    def test_2(self):
        self.assertEqual(True, is_balanced('[()]{}'))

    def test_3(self):
        self.assertEqual(False, is_balanced('({[)]'))

    def test_4(self):
        self.assertEqual(True, is_balanced(''))

    def test_5(self):
        self.assertEqual(False, is_balanced('([]}'))


if __name__ == '__main__':
    unittest.main()
