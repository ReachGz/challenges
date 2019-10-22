"""
[Daily Problem] Longest Substring Without Repeating Characters1

Given a string, find the length of the longest substring without repeating characters.
Can you find a solution in linear time?
"""


def longest_substring_length(s):
    chars = {}
    start = 1
    max_length = 1

    for curr_pos, curr_char in enumerate(s, 1):
        if curr_char in chars:
            length = curr_pos - start
            start = max(chars[curr_char] + 1, start)

            if length > max_length:
                max_length = length

        chars[curr_char] = curr_pos

    return max_length
