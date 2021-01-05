# Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem


def sherlockAndAnagrams(s):
    countDict = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            dictStr = ''.join(sorted(list(s[i:j])))
            countDict[dictStr] = 1 + countDict.get(dictStr, -1)

    count = 0
    for value in countDict.values():
        count += sum(list(range(0, value + 1)))

    return count


sherlockAndAnagrams('bbbb')
