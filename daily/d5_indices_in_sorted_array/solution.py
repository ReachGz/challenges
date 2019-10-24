"""
[Daily Problem] First and Last Indices of an Element in a Sorted Array

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences
of a target element, x. Return -1 if the target is not found.

Example:

Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
"""


def get_range(arr, target):
    # The general idea is to use binary searches with a custom comparison
    # function to cover the case for duplicated values. We have two comparison
    # functions: one that recurses to the left and one to the right.

    first = _binary_search(arr, target, 0, len(arr) - 1, _comparison_first)
    last = _binary_search(arr, target, 0, len(arr) - 1, _comparison_last)

    return [first, last]


def _binary_search(arr, target, left, right, cmp):
    if left > right:
        return -1

    idx = int((right + left) / 2)

    if arr[idx] == target:
        # here we found the target, we need to check if there's duplicates to
        #  the left and to the right using the comparison function (cmp)
        return cmp(arr, target, left, right, idx)

    elif arr[idx] > target:
        return _binary_search(arr, target, left, idx - 1, cmp)

    elif arr[idx] < target:
        return _binary_search(arr, target, idx + 1, right, cmp)


# noinspection PyUnusedLocal
def _comparison_first(arr, target, left, right, idx):
    if idx > 0 and arr[idx - 1] == target:
        # if the previous element is equal to the current one we assume that
        # the current one is greater than the previous, so that we can search
        # for the first occurrence
        return _binary_search(arr, target, left, idx - 1, _comparison_first)
    else:
        return idx


# noinspection PyUnusedLocal
def _comparison_last(arr, target, left, right, idx):
    if idx < len(arr) and arr[idx + 1] == target:
        # similar to _comparison_first() but to search for the last occurrence
        return _binary_search(arr, target, idx + 1, right, _comparison_last)
    else:
        return idx
