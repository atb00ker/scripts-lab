from graph import Graph

if __name__ == "__main__":
    # Sample Input:
    # 1
    # 8 7
    # 0 1 0 2 1 3 4 1 6 4 5 6 5 2 6 0
    numOfinputs = int(input())
    for _ in range(numOfinputs):
        E, V = map(int, input().split())
        dataList = []
        dInput = list(map(int, input().split()))
        for index in range(0, 2*V, 2):
            dataList.append([dInput[index], dInput[index+1]])
        graph = Graph(E, V, dataList, False)
        transitive = graph.transitiveClosure(E)
        for edge in transitive:
            print(*edge, sep=" ")
