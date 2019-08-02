# Google Kickstart
# Question: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051061/0000000000161426


def pairORSum(arr):
    n = len(arr)
    ans = arr[0]
    for i in range(1, n):
        ans = ans ^ arr[i]
    return str(bin(ans))


def countOnes(xorSum):
    count = 0
    for i in xorSum:
        if i == '1':
            count += 1
    return count


def largestEvenXor(arr, n):
    largest = 0
    for i in range(0, n):
        xorSum = pairORSum(arr[:i+1])
        # print(xorSum, len(arr[:i+1]), arr[:i+1])
        count = countOnes(xorSum[2:])
        if count % 2 == 0:
            largest = max(len(arr[:i+1]), largest)
    for i in range(1, n):
        xorSum = pairORSum(arr[i:])
        # print(xorSum, len(arr[i:]), arr[i:])
        count = countOnes(xorSum[2:])
        if count % 2 == 0:
            largest = max(len(arr[i:]), largest)
    return str(largest)


if __name__ == "__main__":
    T = int(input())
    for testcase in range(T):
        largests = []
        details = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        for change in range(details[1]):
            changeList = list(map(int, input().split()))
            arr[changeList[0]] = changeList[1]
            ans = largestEvenXor(arr, details[0])
            largests.append(ans)
        print("Case #", str(testcase+1), ": ", ' '.join(largests), sep="")
