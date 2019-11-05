"""
[Daily Problem] Floor and Ceiling of a Binary Search Tree

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger
than or equal to) of k. If either does not exist, then print them as None.
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_ceiling_floor(root, k, floor=None, ceil=None):
    if root is None:
        return floor, ceil

    if root.value == k:
        return root.value, root.value
    elif root.value > k:
        return find_ceiling_floor(root.left, k, floor, root.value)
    elif root.value < k:
        return find_ceiling_floor(root.right, k, root.value, ceil)
