#!/bin/python3
# https://www.hackerrank.com/contests/w37/challenges/dynamic-line-intersection/problem

def dynamic_line_intersection(input_lines):
    r = []
    i = 0
    lines = {}

    for input_line in input_lines:
        input_line = input_line.split()

        if input_line[0] == '+':
            _, k, b = input_line
            key = get_key(k, b)

            if key in lines:
                lines[key][2] += 1
            else:
                lines[key] = [int(k), int(b), 1]

        elif input_line[0] == '-':
            _, k, b = input_line
            key = get_key(k, b)

            lines[key][2] -= 1

            if lines[key][2] == 0:
                del lines[key]

        elif input_line[0] == '?':
            q = int(input_line[1])
            intersections = 0
            i += 1

            for v in lines.values():
                k, b, c = v
                x = (q - b) / k

                if x.is_integer():
                    intersections += c

            r.append(intersections)

    return r


def get_key(k, b):
    return k + '-' + b


if __name__ == '__main__':
    n = int(input())

    def gen():
        for _ in range(n):
            yield input().strip()

    dynamic_line_intersection(gen())
