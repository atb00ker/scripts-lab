#!/bin/python3
# Question: https://www.hackerrank.com/challenges/special-palindrome-again/problem


def isPalen(wstr):
    wlen = (len(wstr) // 2) + 1
    for i in range(1, wlen):
        if wstr[:i] != wstr[-i:]:
            return False
    return True


def allSubsets(s, setlen, subsets=[]):
    i, slen = 0, len(s)
    while i + setlen <= slen:
        subsets.append(s[i: i + setlen])
        i += 1
    if setlen is not 1:
        allSubsets(s, setlen-1, subsets)
    return subsets


def subSets(s):
    count = 0
    subsets = allSubsets(s, len(s))
    for element in subsets:
        if isPalen(element):
            count += 1
    return count


if __name__ == "__main__":
    mstr = "asasd"
    print(subSets(mstr))
