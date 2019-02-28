# Google Intership Interview 2019
# Check and make product key valid

import bisect
import math


def solution(K, X, Y):
    # Smallest list will save the distances
    # of the devices in sorted order.
    smallestList = []
    lRange = len(X)
    for i in range(lRange):
        xi = X[i]**2
        yi = Y[i]**2
        distance = math.sqrt(xi+yi)
        bisect.insort(smallestList, distance)

    return math.ceil(smallestList[K-1])


K = 4
X = [-1, 2, -4, 2, 4]
Y = [1, 2, -4, 2, -1]

print(solution(K, X, Y))
