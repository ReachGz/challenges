"""
[Daily Problem] Sorting a list with 3 unique numbers

Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list using constant space.
"""
from collections import defaultdict


def sort_nums(nums):
    count = defaultdict(int)

    for e in nums:
        count[e] += 1

    r = []
    r.extend([1] * count[1])
    r.extend([2] * count[2])
    r.extend([3] * count[3])

    return r
