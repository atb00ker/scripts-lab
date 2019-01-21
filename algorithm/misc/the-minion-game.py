#!/bin/python3
# Question: https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    stuart = kevin = vowel = consonants = 0
    lenstr = len(string)
    for i in range(0, lenstr):
        if string[i] in ['A', 'E', 'I', 'O', 'U']:
            vowel += 1
        else:
            consonants += 1
        kevin += vowel
        stuart += consonants
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin " + str(kevin))
    else:
        print("Stuart " + str(stuart))


if __name__ == '__main__':
    minion_game("ANANAS")
