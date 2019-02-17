#!/bin/python3
# Twitter 2019 Internship Coding Interview Round

from bisect import bisect_left


def precomputation(posList, s):
    for index, item in enumerate(s):
        storeIndex = ord(item)-97
        posList[storeIndex].append(index)


def closest(s, queries):
    posList = [[] for i in range(26)]
    resultList = []
    precomputation(posList, s)
    for query in queries:
        qChar = ord(s[query])-97
        posListLen = len(posList[qChar])
        # No other element
        if posListLen < 2:
            resultList.append(-1)
            continue
        # More such elements exist
        qListIndex = bisect_left(posList[qChar], query)
        if qListIndex == 0:
            resultList.append(posList[qChar][qListIndex + 1])
            continue
        elif qListIndex == posListLen - 1:
            resultList.append(posList[qChar][qListIndex - 1])
            continue
        closestBefore = posList[qChar][qListIndex - 1]
        closestAfter = posList[qChar][qListIndex + 1]
        # print(posList[qChar], closestAfter, closestBefore, query)
        diffBefore = query - closestBefore
        diffAfter = closestAfter - query
        # print(diffBefore, diffAfter)
        if diffBefore > diffAfter:
            resultList.append(closestAfter)
            continue
        resultList.append(closestBefore)
    return resultList


if __name__ == '__main__':
    print(closest("hackerranka", [7]))
