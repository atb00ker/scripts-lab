# Graph: https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1


class UndirectedGraph:
    def __init__(self, E, V, dataList):
        self.conn = [[] for _ in range(E)]
        for item in dataList:
            self.conn[item[0]].append(item[1])
            self.conn[item[1]].append(item[0])

    def depthTraversal(self, index, visited=[]):
        nodes = self.conn[index]
        print(index, end=" ")
        for node in nodes:
            if node not in visited:
                visited.append(node)
                self.depthTraversal(node, visited)

    def dfs(self, index):
        print("")
        self.depthTraversal(index, [index])


if __name__ == "__main__":
    # Sample Input:
    # 2
    # 5 4
    # 0 1 0 2 0 3 2 4
    # 4 3
    # 0 1 1 2 0 3
    numOfinputs = int(input())
    for _ in range(numOfinputs):
        E, V = map(int, input().split())
        dataList = []
        dInput = list(map(int, input().split()))
        for index in range(0, 2*V, 2):
            dataList.append([dInput[index], dInput[index+1]])
        graph = UndirectedGraph(E, V, dataList)
        graph.dfs(0)
