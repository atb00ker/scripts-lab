#!/bin/python3
# Question: https://www.hackerrank.com/challenges/new-year-chaos/problem


def minimumBribes(q):
    bribes = 0
    qlen = len(q)
    for i in range(0, qlen):
        if q[i] - i+1 > 4:
            print("Too chaotic")
            return 0
    for i in range(0, qlen):
        swaped = False
        innerQlen = qlen - i - 1
        for i in range(innerQlen):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                bribes += 1
                swaped = True
        if not swaped:
            break
    print(bribes)


if __name__ == '__main__':
    minimumBribes([2, 1, 5, 3, 4])
