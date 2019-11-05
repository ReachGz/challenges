import unittest

from daily.d11_floor_and_ceiling.solution import Node, find_ceiling_floor


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual((4, 6), find_ceiling_floor(self.get_test_tree(), 5))

    def test_2(self):
        self.assertEqual((4, 4), find_ceiling_floor(self.get_test_tree(), 4))

    def test_3(self):
        self.assertEqual((2, 2), find_ceiling_floor(self.get_test_tree(), 2))

    def test_4(self):
        self.assertEqual((2, 4), find_ceiling_floor(self.get_test_tree(), 3))

    def test_5(self):
        self.assertEqual((6, 8), find_ceiling_floor(self.get_test_tree(), 7))

    def test_6(self):
        self.assertEqual((8, 10), find_ceiling_floor(self.get_test_tree(), 9))

    def test_7(self):
        self.assertEqual((None, 2), find_ceiling_floor(self.get_test_tree(), 1))

    def test_8(self):
        self.assertEqual((14, None), find_ceiling_floor(self.get_test_tree(), 15))

    @staticmethod
    def get_test_tree():
        """
        Returns a tree like this one:
               8
               |
           ---------
           |       |
           4       12
           |       |
        -----    -----
        |   |    |   |
        2   6   10  14
        """
        root = Node(8)
        root.left = Node(4)
        root.right = Node(12)

        root.left.left = Node(2)
        root.left.right = Node(6)

        root.right.left = Node(10)
        root.right.right = Node(14)

        return root


if __name__ == '__main__':
    unittest.main()
