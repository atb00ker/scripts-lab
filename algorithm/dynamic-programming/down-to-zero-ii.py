#!/bin/python3
# Question: https://www.hackerrank.com/challenges/down-to-zero-ii/problem

import os
import sys


def precomputation():
    possNumbs[0], possNumbs[1], possNumbs[2], possNumbs[3] = 0, 1, 2, 3
    for outerNumb in range(2, numRange):
        if possNumbs[outerNumb] == -1 or possNumbs[outerNumb] > possNumbs[outerNumb-1]+1:
            possNumbs[outerNumb] = possNumbs[outerNumb-1] + 1
        inclusiveRange = outerNumb + 1
        for innerNumb in range(2, inclusiveRange):
            newNumb = outerNumb*innerNumb
            if newNumb >= numRange:
                break
            if possNumbs[newNumb] == -1 or possNumbs[newNumb] > possNumbs[outerNumb] + 1:
                possNumbs[newNumb] = possNumbs[outerNumb] + 1


def downToZero(n):
    return possNumbs[n]


if __name__ == '__main__':
    numRange = 1000001
    possNumbs = [-1] * numRange
    precomputation()

    # Custom Testcase #0
    testcases = [30, 150, 2970, 168, 195, 156, 300000, 13, 44, 100, 169]
    for testcase in testcases:
        print(downToZero(testcase))

    # Bought testcase #1 from hackerrank
    testcases = [94, 966514, 812849, 808707, 360422, 691410, 691343, 551065, 432560, 192658, 554548, 27978, 951717, 663795, 315528, 522506, 300432, 412509, 109052, 614346, 589115, 301840, 7273, 193764, 702818, 639354, 584658, 208828, 255463, 506460, 471454, 554516, 739987, 303876, 813024, 118681, 708473, 616288, 962466, 55094, 599778, 385504, 428443, 646717, 572077, 463452, 750219, 725457, 672957, 750371, 542716, 87017, 743756, 293742, 301031, 939025, 503398, 334595, 209039, 191818, 158563, 617470, 118260, 176581, 966721, 48924, 235330, 200174, 992221, 411098, 559560, 117381, 814728, 795418, 309832, 943111, 775314, 875208, 168234, 933574, 444474, 995856, 687362, 543687, 761831, 952514, 970724, 611269, 237583, 88891, 708888, 387629, 407891, 393991, 577592]
    for testcase in testcases:
        print(downToZero(testcase))
