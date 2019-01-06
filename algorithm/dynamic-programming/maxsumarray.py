#!/bin/python3
# Question: https://www.hackerrank.com/challenges/maxsubarray/problem

import os
import sys


# O(n) with the help of Kadane's algorithm
def maxSubarray(arr):
    size = len(arr)
    local_max = arr[0]
    global_max = arr[0]
    max_positive = arr[0]

    for i in range(1, size):
        current_max = local_max + arr[i]
        local_max = max(current_max, arr[i])
        global_max = max(global_max, local_max)
        if arr[i] > 0 and max_positive > 0:
            max_positive += arr[i]
        elif arr[i] > max_positive:
            max_positive = arr[i]

    return "%d %d" % (global_max, max_positive)


if __name__ == '__main__':
    print(maxSubarray([2, -1, 2, 3, 4, -5]))
