

from collections import defaultdict, deque


# Find shortest path from s to any node on an unweight graph 
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
    
    def traversal_bfs(self, s):

        visited = [False]*len(self.vertices)
        parent = [None]*len(self.vertices)

        q = deque()
        q.append(s)

        visited[s] = True

        while q:

            u = q.popleft()

            for v in self.adj[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v] = True
                    parent[v] = u
        
        return parent

    def reconstruct_path(self, s, e, parent):

        path = []

        v = e

        path.append(v)
        
        while True:
            v = parent[v]
           
            if v is None:
                break
        
            path.append(v)
            
        
        path.reverse()

        if path[0] == s:
            return path
        
        return []
        
    def bfs(self, s, e):
        
        parent = self.traversal_bfs(s)

        return self.reconstruct_path(s, e, parent)



g = Graph()
g.add_edge(0, 7)
g.add_edge(0, 11)
g.add_edge(1, 8)
g.add_edge(0, 9)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 2)
g.add_edge(6, 5)
g.add_edge(7, 11)
g.add_edge(7, 6)
g.add_edge(7, 3)
g.add_edge(8, 1)
g.add_edge(8, 12)
g.add_edge(9, 8)
g.add_edge(9, 10)
g.add_edge(10, 1)
g.add_edge(12, 2)

print(g.bfs(0, 4))
print(g.bfs(9, 2))
print(g.bfs(2, 11))
print(g.bfs(8, 4))
print(g.bfs(0, 5))
print(g.bfs(3, 1))


