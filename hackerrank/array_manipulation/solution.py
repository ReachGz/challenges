#!/bin/python3
# https://www.hackerrank.com/challenges/crush/problem


def array_manipulation(n, queries):
    arr = [0] * (n + 1)
    max_num = -1

    for q in queries:
        a, b, k = q
        for i in range(a, b + 1):
            arr[i] += k
            if arr[i] > max_num:
                max_num = arr[i]

    return max_num


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)
    print(result)
