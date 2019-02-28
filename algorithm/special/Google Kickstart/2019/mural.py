# Google Kickstart 2019 Round: Practice

import math


def solution(N, K):
    paintLen, subarraySum, globalMax = math.ceil(N / 2), 0, 0
    for i in range(paintLen):
        subarraySum += int(K[i])
    globalMax = max(globalMax, subarraySum)

    for i in range(paintLen, N):
        subarraySum += int(K[i])
        subarraySum -= int(K[i-paintLen])
        globalMax = max(globalMax, subarraySum)

    return str(globalMax)


def muralPaint():
    T = int(input())
    N, K = [0]*T, [0]*T
    for i in range(T):
        N[i] = int(input())
        K[i] = str(input())
    for i in range(T):
        print("Case #" + str(i+1) + ": " + solution(N[i], K[i]))


muralPaint()
# solution(2, 3, 1, 2, 1, 2, 1, 1, 9)
# solution(10, 10, 10001, 10002, 10003, 10004, 10005, 10006, 89273)
