"""
[Daily Problem] Reverse a Linked List

Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        node = self
        output = ''

        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next

        return output


def reverse_iterative(head):
    node = head
    stack = []

    while node.next is not None:
        stack.append(node)
        node = node.next

    new_head = node

    while stack:
        node.next = stack.pop()
        node = node.next

    node.next = None
    return new_head


def reverse_recursive(head):
    head, _ = _reverse_recursive_impl(head)
    return head


def _reverse_recursive_impl(head):
    if head.next is None:
        r = ListNode(head.val)
        return r, r
    else:
        new_head, r = _reverse_recursive_impl(head.next)
        r.next = ListNode(head.val)
        return new_head, r.next
