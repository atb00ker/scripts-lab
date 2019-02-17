#!/bin/python3
# Twitter 2019 Internship Coding Interview Round


def textQueries(sentences, queries):
    sDict = dict()
    for sIndex in range(len(sentences)):
        sDict[sIndex] = set(sentences[sIndex].split())

    for query in queries:
        qList = query.split()
        remainList = []
        for sIndex in range(len(sDict)):
            qCount = len(qList)
            for qElement in qList:
                if qElement not in sDict[sIndex]:
                    break
                qCount -= 1
            if qCount == 0:
                remainList.append(sIndex)
                if len(remainList) > 10:
                    break
        if not remainList:
            print(-1)
        else:
            print(*remainList, sep=" ")


sentences = ["jim likes mary", "kate likes tom", "tom does not like jim"]
# sentences = ["how it was done", "are you how", "it goes to", "goes done are it"]
queries = ["jim tom", "likes"]

textQueries(sentences, queries)
