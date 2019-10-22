"""
[Daily Problem] Longest Palindromic Substring

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s,
find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"
"""


def longest_palindrome(s):
    max_length = -1
    max_string = None
    start = 0
    end = len(s) - 1

    while start < end:
        while start < end:
            if is_palindrome(s, start, end):
                length = end - start

                if length > max_length:
                    max_length = length
                    max_string = s[start:end + 1]

            start += 1

        start = 0
        end -= 1

    return max_string


def is_palindrome(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True
