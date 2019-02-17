#!/bin/python3
# Twitter 2019 Internship Coding Interview Round


def precomputation(sentences, sDict):
    for sIndex in range(len(sentences)):
        wordsInSentence = sentences[sIndex].split()
        for word in wordsInSentence:
            if word in sDict:
                sDict[word].append(sIndex)
                continue
            sDict[word] = [sIndex]


def queryResult(sDict, query):
    qList = query.split()
    querysetList = []

    for qElement in qList:
        if qElement not in sDict:
            return [-1]
        querysetList.append(set(sDict[qElement]))

    if querysetList:
        resultSet = set.intersection(*querysetList)
        if resultSet:
            return sorted(resultSet)
    return [-1]


def textQueries(sentences, queries):
    sDict = dict()
    # Create a word: sentences dictionary
    precomputation(sentences, sDict)
    for query in queries:
        print(*queryResult(sDict, query), sep=" ")


sentences = ["how it was done home", "are you how",
             "it goes to home", "home goes done are it", "goes goes"]
queries = ["it goes home", "braker", "down in london", "it goes done goes", ""]

textQueries(sentences, queries)
