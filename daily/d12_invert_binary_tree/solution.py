"""
[Daily Problem] Invert a Binary Tree

You are given the root of a binary tree. Invert the binary tree in place. That is, all left children should become
right children, and all right children should become left children.

Example:

      a
      |
  ---------
  |       |
  b       c
  |       |
-----   -----
|   |   |   |
d   e   f

The inverted version of this tree is as follows:

      a
      |
  ---------
  |       |
  c       b
  |       |
-----   -----
|   |   |   |
    f   e   d
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def pre_order(self):
        r = str(self.value)

        if self.left:
            r = r + ' ' + self.left.pre_order()

        if self.right:
            r = r + ' ' + self.right.pre_order()

        return r


def invert(node):
    if node is None:
        return

    node.left, node.right = node.right, node.left
    invert(node.right)
    invert(node.left)
