"""
[Daily Problem] Find the non-duplicate number

Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

Challenge: Find a way to do this using O(1) memory. ToDo
"""


def single_number_1(nums):
    existing = {}

    for e in nums:
        if e in existing:
            del existing[e]
        else:
            existing[e] = True

    return existing.popitem()[0]


def single_number_2(nums):
    size = len(nums)

    for i in range(size):
        found = False

        for j in range(size):
            if i != j and nums[i] == nums[j]:
                found = True
                break

        if not found:
            return nums[i]


single_number = single_number_1
