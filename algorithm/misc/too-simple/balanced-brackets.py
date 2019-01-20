#!/bin/python3
# Question: https://www.hackerrank.com/challenges/balanced-brackets/problem

import os


def isBalanced(s):
    seenStack = []
    for charater in s:
        if charater in ["{", "[", "("]:
            seenStack.append(charater)
        elif seenStack:
            last_element = seenStack[-1]
            if (charater is "}" and last_element is "{") \
                    or (charater is ")" and last_element is "(") \
                    or (charater is "]" and last_element is "["):
                seenStack.pop()
            else:
                return "NO"
        else:
            return "NO"

    if seenStack:
        return "NO"
    return "YES"


if __name__ == '__main__':
    for s in ["{[()]}", "{[(])}", "{{[[(())]]}}", "", "))]]}}"]:
        print(isBalanced(s))
