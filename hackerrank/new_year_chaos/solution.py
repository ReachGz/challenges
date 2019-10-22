#!/bin/python3
# https://www.hackerrank.com/challenges/new-year-chaos/problem

def minimum_bribes(q):
    size = len(q)
    r = 0

    # first check that the position is valid i.e. that nobody bribed
    # more than twice
    for i, e in enumerate(q):
        diff = e - i - 1

        if diff > 2:
            return "Too chaotic"

    # then, for each person check how many people he passed
    for i in range(size):
        for j in range(i + 1, size):
            if q[j] < q[i]:
                r += 1

    return r


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        print(minimum_bribes(q))
