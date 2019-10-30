"""
[Daily Problem] Two-Sum

You are given a list of numbers, and a target number k. Return whether or not there are two numbers in
the list that add up to k.

Example:
Given [4, 7, 1, -3, 2] and k = 5,
return true since 4 + 1 = 5.

Try to do it in a single pass of the list.
"""


def two_sum_dynamic(a_list, k, n=2, i=None):
    if k == 0:
        return True

    if i is None:
        i = len(a_list) - 1

    if n <= 0 or i < 0:
        return False

    include = two_sum_dynamic(a_list, k - a_list[i], n - 1, i - 1)
    exclude = two_sum_dynamic(a_list, k, n, i - 1)

    return include or exclude


def two_sum_linear(a_list, k):
    m = {}

    for e in a_list:
        diff = k - e

        if diff in m:
            return True
        else:
            m[e] = True

    return False


two_sum = two_sum_linear
