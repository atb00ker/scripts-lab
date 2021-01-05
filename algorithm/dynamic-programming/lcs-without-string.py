# https://www.hackerrank.com/challenges/common-child/problem


def longestCommonSubsequence(s1, s2):
    remove_element = set(s1) - set(s2)
    new_s1 = ""
    for element in s1:
        if element not in remove_element:
            new_s1 += element
    s1 = new_s1

    memory = [[0] * (len(s2) + 1) for _ in range((len(s1) + 1))]
    for index1, value1 in enumerate(s1, 1):
        for index2, value2 in enumerate(s2, 1):
            if value1 == value2:
                memory[index1][index2] = memory[index1 - 1][index2 - 1] + 1
            else:
                memory[index1][index2] = max(
                    memory[index1 - 1][index2], memory[index1][index2 - 1]
                )

    return memory[-1][-1]


print(longestCommonSubsequence("HARRY", "SALLY"))
