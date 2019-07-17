#!/bin/python3
# Question: https://www.hackerrank.com/challenges/special-palindrome-again/problem


def substrCount(n, s):
    countList, elementList, count, prevElement, result = [], [], 0, s[0], 0
    for index in range(n):
        if s[index] == prevElement:
            count += 1
        else:
            result += count*(count+1)/2
            countList.append(count)
            elementList.append(s[index-1])
            count = 1
        prevElement = s[index]
    result += count*(count+1)/2
    countList.append(count)
    elementList.append(s[index])

    print(result, countList, elementList, count)

    clen = len(countList)-1
    for index in range(1, clen):
        if countList[index] == 1 and elementList[index-1] == elementList[index+1]:
            print(index)
            result += min(countList[index-1], countList[index+1])

    print(result, countList, elementList, count)

    return int(result)


if __name__ == "__main__":
    mstr = "acbac"
    print(substrCount(len(mstr), mstr))
    # Assets#1
    # import random
    # options = "abc"
    # while True:
    #     mstr = ""
    #     for _ in range(5):
    #         mstr += options[random.randrange(3)]
    #     if substrCount(len(mstr), mstr) != CountSpecialPalindrome(len(mstr), mstr):
    #         print(mstr)
    #         break
