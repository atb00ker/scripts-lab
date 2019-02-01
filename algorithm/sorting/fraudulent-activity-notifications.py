#!/bin/python3
# Question: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

import bisect


def getMedian(half, sortedForMedian):
    if not len(sortedForMedian) % 2:
        return (sortedForMedian[half - 1] + sortedForMedian[half]) / 2.0
    return sortedForMedian[half]


def activityNotifications(expenditure, d):
    alerts = 0
    half = d // 2

    # Sorting #1
    sortedForMedian = sorted(expenditure[0:d-1])
    # Check Alerts #1
    nextDay = expenditure[d]
    medianSoFar = getMedian(half, sortedForMedian)
    if medianSoFar*2 <= nextDay:
        alerts += 1

    for i in range(len(expenditure)-d-1):
        # Sorting
        sortedForMedian.remove(expenditure[i])
        bisect.insort_left(sortedForMedian, nextDay)
        # Check Alerts
        nextDay = expenditure[d+i+1]
        medianSoFar = getMedian(half, sortedForMedian)
        if medianSoFar*2 <= nextDay:
            alerts += 1

    return alerts


if __name__ == '__main__':
    # print(activityNotifications([10, 20, 30, 40, 50], 3))
    print(activityNotifications([1, 2, 3, 4, 4], 4))
