# Graph: https://practice.geeksforgeeks.org/problems/print-adjacency-list/0


class UndirectedGraph:
    def __init__(self, E, V, dataList):
        self.conn = [[] for _ in range(E)]
        for item in dataList:
            self.conn[item[0]].append(item[1])
            self.conn[item[1]].append(item[0])


def adjacencyList(vert):
    for index, items in enumerate(vert):
        if items:
            print(index, "-> ",
                  "-> ".join(str(item) for item in items),
                  sep='')
        else:
            print(index)


if __name__ == "__main__":
    numOfinputs = int(input())
    for _ in range(numOfinputs):
        E, V = map(int, input().split())
        dataList = []
        for _ in range(V):
            dList = list(map(int, input().split()))
            dataList.append(dList)
        graph = UndirectedGraph(E, V, dataList)
        adjacencyList(graph.conn)
