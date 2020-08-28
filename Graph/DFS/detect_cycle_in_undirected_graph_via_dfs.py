from collections import defaultdict


'''
HATALI, EKSIK 
'''
class Graph:

    def __init__(self):

        self.adj = defaultdict(list)
        self.vertices = []
    
    

    def add_edge(self, u, v):

        #undirected graph
        self.adj[u].append(v) 
        self.adj[v].append(u)

        if u not in self.vertices: 
            self.vertices.append(u)
        
        if v not in self.vertices:
            self.vertices.append(v)
        

    def is_cyclic_util(self, v, visited, parent):

        visited[v] = True

        for i in self.adj[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True

            elif parent != i:
                return True

        return False

    def is_cyclic(self):


        visited = [False]*len(self.vertices)


        for i in range(len(self.vertices)):

            if not visited[i]:

                if self.is_cyclic_util(i, visited, -1):
                    return True
        
        return False

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

if g.is_cyclic():

    print("g graph contains cycle")

else:
    print("g graph does not contain cycle")
