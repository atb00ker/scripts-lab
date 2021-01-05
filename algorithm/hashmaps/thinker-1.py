# https://www.hackerrank.com/challenges/count-triplets-1/problem


def countTriplets(arr, r):
    count = 0
    dictSeen = {}
    dictPairs = {}

    for a in reversed(arr):
        next_prog_element = a * r
        if next_prog_element in dictPairs:
            count += dictPairs[next_prog_element]
        if next_prog_element in dictSeen:
            dictPairs[a] = dictPairs.get(a, 0) + dictSeen[next_prog_element]
        dictSeen[a] = dictSeen.get(a, 0) + 1
    return count


print(countTriplets([8, 24, 72], 3))
