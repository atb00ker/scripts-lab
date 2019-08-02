# Goldman Sachs
# Question: https://che.gg/2OJZJnk

from collections import Counter


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high][1]
    for j in range(low, high):
        if arr[j][1] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def trueNum(mapping, num):
    gStr = ""
    for i in str(num):
        mapVal = mapping.index(int(i))
        gStr += str(mapVal)
    return int(gStr)


def strangeSort(mapping, nums):
    # Write your code here
    flist, valList = [], []
    for num in nums:
        val = trueNum(mapping, num)
        valList.append(tuple((num, val)))
    quickSort(valList, 0, len(valList)-1)
    print(valList)
    for val in valList:
        flist.append(val[0])
    return flist


if __name__ == "__main__":
    mapping = [2, 1, 6, 4, 3, 5, 9, 8, 7, 0]
    nums = ['321', '32', '032', '12', '42', '03', '03']
    strangeSort(mapping, nums)
