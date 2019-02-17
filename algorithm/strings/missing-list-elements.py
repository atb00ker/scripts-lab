#!/bin/python3
# Twitter 2019 Internship Coding Interview Round

def missingWords(s, t):
    sList = s.split()
    tList = t.split()
    nList = []
    j = 0
    tLen = len(tList)
    for index, item in enumerate(sList):
        if item == tList[j]:
            j += 1
            if j == tLen:
                nList += sList[index+1:]
                break
        else:
            nList.append(item)

        return nList


s = "I am using HackerRank to improve programming"
t = "am HackerRank to improve"
missingWords(s, t)
