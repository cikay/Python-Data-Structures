from collections import defaultdict

# hatali eksik
class Graph:

    def __init__(self):

        self.adj = defaultdict(list)
        self.vertices = []

    
    def add_edge(self, u, v):

        self.adj[u].append(v)

        if v not in self.vertices:
            self.vertices.append(v)

        if u not in self.vertices:
            self.vertices.append(u)
        
    

    def topological_sort_traversal(self, s, visited, stack):

        visited[s] = True

        for v in self.adj[s]:

            if not visited[v]:
                self.topological_sort_traversal(v, visited, stack)
        

        
        stack.insert(0, s)

    
    def topological_sort(self):

        visited = [False]*len(self.vertices)

        stack = []

        for i in range(len(self.vertices)):
            if not visited[i]:
                self.topological_sort_traversal(i, visited, stack)


        print(stack)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.topological_sort()






'''
#Python program to print topological sorting of a DAG 
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print(stack) 
  
g= Graph(6) 
g.addEdge(3, 1)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)

  

g.topologicalSort() 
#This code is contributed by Neelam Yadav 
'''