"""
[Daily Problem] Add two numbers as a linked list

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and
each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        r = ''
        curr = self

        while curr:
            r += str(curr.val)
            curr = curr.next

        return r

    def add(self, other):
        return add_two_numbers(self, other)


def add_two_numbers(l1, l2, carry=0):
    op1 = 0 if l1 is None else l1.val
    op2 = 0 if l2 is None else l2.val
    t = op1 + op2 + carry

    if t == 0:
        return None

    new_carry = int(t / 10)
    curr = t % 10
    r = ListNode(curr)

    r.next = add_two_numbers(
        None if l1 is None else l1.next,
        None if l2 is None else l2.next,
        new_carry
    )

    return r
