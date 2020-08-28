from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.adj = defaultdict(list)
        self.vertices = []

    def add_edge(self, u, v):

        self.adj[u].append(v)
        self.adj[v].append(u)

        if u not in self.vertices:
            self.vertices.append(u)
        
        if v not in self.vertices:
            self.vertices.append(v)
    
    
    def contain_cyclic(self):

        parent = [-1]*len(self.vertices)

        visited = [False]*len(self.vertices)

        s = self.vertices[0]
        q = deque()

        visited[s] = True
        q.append(s)


        while q:

            u = q.pop()

            for v in self.adj[u]:

                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    parent[v] = u

                elif parent[u] != v:
                    return True

        return False




g = Graph()

# TEST 1
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 0)

# # TEST 2 --

# g.add_edge(1, 0)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)



# # TEST 3 --

# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 0)


# # TEST 4 --
g.add_edge(0, 7)
g.add_edge(0, 11)
g.add_edge(0, 9)
g.add_edge(1, 8)
g.add_edge(3, 4)
g.add_edge(6, 5)
g.add_edge(7, 6)
g.add_edge(7, 3)
g.add_edge(8, 12)
g.add_edge(9, 10)
g.add_edge(10, 1)
g.add_edge(12, 2)


if g.contain_cyclic():
    print("the graph contain at least one cycle")
else:
    print("the graph contain no cycles")