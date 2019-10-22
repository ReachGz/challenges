"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the
program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using
strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:

Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""


def is_balanced(s):
    m = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    opening = m.values()
    closing = m.keys()
    stack = []

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            actual = stack.pop()
            expected = m[char]

            if actual != expected:
                return False

    return not stack
