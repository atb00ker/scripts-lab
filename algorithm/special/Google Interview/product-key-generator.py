# Google Intership Interview 2019
# Check and make product key valid


def solution(S, K):
    N = ""
    dAdjust = 1
    for i, element in enumerate(S[::-1]):
        if element == "-":
            dAdjust -= 1
        else:
            N += element.upper()
        if not (i+dAdjust) % 4:
            N += "-"

    if N[-1] == "-":
        N = N[:-1]
    return N[::-1]


S = "2-4A0r7-4k"
solution(S, 4)
