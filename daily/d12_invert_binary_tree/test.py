import unittest

from daily.d12_invert_binary_tree.solution import Node, invert


class MyTestCase(unittest.TestCase):
    def test_1(self):
        root = Node('a')
        root.left = Node('b')
        root.right = Node('c')
        root.left.left = Node('d')
        root.left.right = Node('e')
        root.right.left = Node('f')

        self.assertEqual('a b d e c f', root.pre_order())
        invert(root)
        self.assertEqual('a c f b e d', root.pre_order())


if __name__ == '__main__':
    unittest.main()
