#!/bin/python3


def insertionSort(ar, start, end):
    for i in range(start, end):
        temp = ar[i]
        j = i - 1
        while (ar[j] > temp and j >= start):
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = temp


def mergeSort(ar, start, middle, end):
    sortedAr = []
    firstAr = ar[start:middle]
    secondAr = ar[middle:end]
    pointerFirstAr = pointerSecondAr = 0

    while firstAr and secondAr:
        if firstAr[0] < secondAr[0]:
            sortedAr.append(firstAr.pop(0))
        else:
            sortedAr.append(secondAr.pop(0))

    if pointerFirstAr < middle:
        sortedAr.extend(firstAr[pointerFirstAr:])
    if pointerSecondAr < end:
        sortedAr.extend(secondAr[pointerSecondAr:])

    for i in range(start, end):
        ar[i] = sortedAr[i-start]


def timSort(ar, n, isort):

    for i in range(0, n, isort):
        insertionSort(ar, i, min(i+isort, n))

    while isort < n:
        for i in range(0, n, isort*2):
            mid = i+isort
            end = min(mid+isort, n)
            if end > mid:
                mergeSort(ar, i, mid, end)
        isort *= 2
    print(ar)


if __name__ == '__main__':
    ar = [42, 2, 1, 5, 32, 3, 4, 36, 21, 25, 66, 12, 15, 17, 40]
    isort = 11
    timSort(ar, len(ar), isort)
