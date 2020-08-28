
from collections import defaultdict


class Graph:

    def __init__(self):

        self.adj = defaultdict(list)
        self.vertices = []


    def add_edge(self, u, v):

        self.adj[u].append(v)

        if u not in self.vertices:
            self.vertices.append(u)

        if v not in self.vertices:
            self.vertices.append(v)


    def dfs_visit(self, s, visited):

        
        print(s)

        visited[s] = True

        for v in self.adj[s]:
            if not visited[v]:
                visited[v] = False
                self.dfs_visit(v, visited)

    def dfs(self, s):

        visited = [False]*(max(self.adj)+1)
        
        for v in self.vertices:
            
            if not visited[v]:

                visited[v] = False
                self.dfs_visit(v, visited)



g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 1)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(0, 1)
g.dfs(2)
