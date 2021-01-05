# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem


def longestCommonSubsequence(b, a):
    matrix = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for index1, value1 in enumerate(a, 1):
        for index2, value2 in enumerate(b, 1):
            if value1 == value2:
                matrix[index1][index2] = matrix[index1 - 1][index2 - 1] + 1
            else:
                matrix[index1][index2] = max(
                    matrix[index1 - 1][index2], matrix[index1][index2 - 1]
                )

    print(end="    ")
    for i in range(len(b)):
        print(b[i], end="  ")
    print()
    for i in range(len(a) + 1):
        print(matrix[i])

    rloc = len(a)
    cloc = len(b)
    output = []
    while rloc > 0 and cloc > 0:
        if matrix[rloc][cloc - 1] == matrix[rloc - 1][cloc]:
            if matrix[rloc][cloc - 1] == matrix[rloc][cloc]:
                cloc -= 1
            else:
                rloc -= 1
                cloc -= 1
                output.append(b[cloc])
        elif matrix[rloc][cloc - 1] > matrix[rloc - 1][cloc]:
            cloc -= 1
        else:
            rloc -= 1

    return output[::-1]


print(longestCommonSubsequence("12341", "341213"))

