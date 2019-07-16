# Graph classes: Functions used
# in a lot of programs for graph


class Graph:
    def __init__(self, E, V, dataList, undirected):
        self.conn = [[] for _ in range(E)]
        for item in dataList:
            self.conn[item[0]].append(item[1])
            if undirected:
                self.conn[item[1]].append(item[0])

    # Utils
    def depthTraversal(self, index, visited, traversed):
        nodes = self.conn[index]
        traversed.append(index)
        for node in nodes:
            if node not in visited:
                visited.append(node)
                self.depthTraversal(node, visited, traversed)
        return traversed

    def breadthTraversal(self, index, visited, inqueue, traversed):
        nodes = self.conn[index]
        for node in nodes:
            if node not in visited:
                traversed.append(node)
        visited.append(index)
        inqueue.extend(nodes)
        while inqueue:
            index = inqueue.pop(0)
            if index not in visited:
                self.breadthTraversal(index, visited, inqueue, traversed)
                break
        return traversed

    # User
    def dfs(self, index):
        return self.depthTraversal(index, [index], [])

    def bfs(self, index):
        return self.breadthTraversal(index, [], [], [index])

    def transitiveClosure(self, edges):
        edges = edges - 1
        transitive = [[0 for _ in range(edges)] for _ in range(edges)]
        for edge in range(edges):
            visited = self.dfs(edge)
            for node in visited:
                transitive[edge][node] = 1
        return transitive
