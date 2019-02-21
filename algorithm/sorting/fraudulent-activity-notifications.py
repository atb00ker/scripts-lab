#!/bin/python3
# Question: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
# Note: Testcase 5 purchased

import bisect


def getMedian(d, half, countingSort, expenditure):
    if not d % 2:
        li, lo = None, None
        for i in range(201):
            if countingSort[i] >= half - 1 and not li:
                li = i
            if countingSort[i] >= half and not lo:
                lo = i
            if li and lo:
                return (li + lo)
    else:
        for i in range(201):
            if half <= countingSort[i]:
                return (i * 2)


def changeCountingSort(countingSort, addValue, removeValue):
    if removeValue > addValue:
        for i in range(addValue, removeValue):
            countingSort[i] += 1
    elif removeValue < addValue:
        for i in range(removeValue, addValue):
            countingSort[i] -= 1


def activityNotifications(expenditure, d):
    alerts = 0
    expLen = len(expenditure)
    half = d // 2
    countingSort = [0] * 201
    # Sorting #1
    for i in expenditure[0:d]:
        countingSort[i] += 1
    sumSoFar = -1
    for i in range(201):
        sumSoFar += countingSort[i]
        countingSort[i] = sumSoFar
    # Check #1
    medianSoFar = getMedian(d, half, countingSort, expenditure)
    if medianSoFar <= expenditure[d]:
        alerts += 1

    for i in range(d, expLen-1):
        removeValue = expenditure[i-d]
        addValue = expenditure[i]
        changeCountingSort(countingSort, addValue, removeValue)
        medianSoFar = getMedian(d, half, countingSort, expenditure)
        if medianSoFar <= expenditure[i+1]:
            alerts += 1
    return alerts


if __name__ == '__main__':
    print(activityNotifications([10, 20, 30, 40, 50], 3))
    print(activityNotifications([1, 2, 3, 4, 4], 4))
