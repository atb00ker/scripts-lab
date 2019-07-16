# Graph: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1


class UndirectedGraph:
    def __init__(self, E, V, dataList):
        self.conn = [[] for _ in range(E)]
        for item in dataList:
            self.conn[item[0]].append(item[1])
            self.conn[item[1]].append(item[0])

    def breadthTraversal(self, index, visited, inqueue):
        nodes = self.conn[index]
        for node in nodes:
            if node not in visited:
                print(" ".join(str(node)), end=" ")
        visited.append(index)
        inqueue.extend(nodes)
        while inqueue:
            index = inqueue.pop(0)
            if index not in visited:
                self.breadthTraversal(index, visited, inqueue)
                break

    def bfs(self, index):
        print(index, end=" ")
        self.breadthTraversal(index, [], [])
        print("")


class DirectedGraph:
    def __init__(self, E, V, dataList):
        self.conn = [[] for _ in range(E)]
        for item in dataList:
            self.conn[item[0]].append(item[1])

    def breadthTraversal(self, index, visited=[], inqueue=[]):
        nodes = self.conn[index]
        for node in nodes:
            print(" ".join(str(node)), end=" ")
        visited.append(index)
        inqueue.extend(nodes)
        while inqueue:
            index = inqueue.pop(0)
            if index not in visited:
                self.breadthTraversal(index, visited, inqueue)
                break

    def bfs(self, index):
        print(index, end=" ")
        self.breadthTraversal(index)
        print("")


if __name__ == "__main__":
    # Sample Input:
    # 2
    # 5 4
    # 0 1 0 2 0 3 2 4
    # 3 2
    # 0 1 0 2
    numOfinputs = int(input())
    for _ in range(numOfinputs):
        E, V = map(int, input().split())
        dataList = []
        dInput = list(map(int, input().split()))
        for index in range(0, 2*V, 2):
            dataList.append([dInput[index], dInput[index+1]])
        graph = DirectedGraph(E, V, dataList)
        graph.bfs(0)
