# Google Kickstart 2019 Round: Practice

def solution(N, K, x1, y1, C, D, E1, E2, F):

    alarmList = []
    alarmPowermap = [[] for i in range(K)]
    alarmPower = 0

    # Calculate alarmList
    element = (x1 + y1) % F
    xPrev, yPrev = x1, y1
    alarmList.append(element)
    for _ in range(N-1):
        xi = (C*xPrev + D*yPrev + E1) % F
        yi = (D*xPrev + C*yPrev + E2) % F
        element = (xi + yi) % F
        xPrev, yPrev = xi, yi
        alarmList.append(element)

    # Calculate Alarm Subsets
    alarmSubset = []
    for i in range(1, N+1):
        for j in range(N-i+1):
            alarmSubset.append(alarmList[j:j+i])

    # Calculate alarmPowermap
    for kthElement in range(K):
        for indexElement in range(1, N+1):
            alarmPowermap[kthElement].append(indexElement**(kthElement+1))

    # Calculate alarmPowerList
    for kthElement in range(K):
        for subset in alarmSubset:
            for index, element in enumerate(subset):
                alarmPower += element*alarmPowermap[kthElement][index]
    return str(alarmPower % 1000000007)


def kickstartAlarm():
    T = int(input())
    N, K, x1, y1, C, D, E1, E2, F = [0]*T, [0]*T, [0] * \
        T, [0]*T, [0]*T, [0]*T, [0]*T, [0]*T, [0]*T
    for i in range(T):
        N[i], K[i], x1[i], y1[i], C[i], D[i], E1[i], E2[i], F[i] = map(
            int, input().split())
    for i in range(T):
        print("Case #" + str(i+1) + ": " +
              solution(N[i], K[i], x1[i], y1[i], C[i], D[i], E1[i], E2[i], F[i]))


kickstartAlarm()

# solution(2, 3, 1, 2, 1, 2, 1, 1, 9)
# solution(10, 10, 10001, 10002, 10003, 10004, 10005, 10006, 89273)
