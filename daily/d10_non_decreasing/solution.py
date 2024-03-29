"""
[Daily Problem] Non-decreasing Array with Single Modification

You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array
non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.
[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array
           non-decreasing.

Can you find a solution in O(n) time?
"""


def non_decreasing(a_list):
    g = 0

    for i in range(len(a_list) - 1):
        if a_list[i] > a_list[i + 1]:
            g += 1

    return g <= 1
