
from collections import defaultdict, deque
import sys

class Graph:

    def __init__(self, is_directed):
        self.adj = defaultdict(list)
        self.vertices = []
        self.__is_directed = is_directed
    

    def add_edge(self, u, v):

        self.adj[u].append(v)

        if not self.__is_directed:
            self.adj[v].append(u)


        if u not in self.vertices:
            self.vertices.append(u)
        
        if v not in self.vertices:
            self.vertices.append(v)
        
    def min_distance(self, dist, spt_set):

        min = sys.maxint

        for v in range(len(self.vertices)):
            if dist[v] < min and spt_set[v] == False:
                min = dist[v]
                min_index = v
        
        return min_index


    def dijkstra(self, start, end):

        dist = [sys.maxint]*len(self.vertices)
        dist[src] = 0
        spt_set = [False]*len(self.vertices)


        # que = deque()
        # que.append(start)


        # while que:

        #     u = que.popleft()

        #     for v in self.adj[u]:
        #         if not visited[v]:
        #             que.append(v)

        for cout in range(len(self.vertices)):

            u = self.min_distance(dist, spt_set)

            spt_set[u] = True

            for v in range(len(self.vertices)):
                if self.adj[u][v] > 0 and spt_set[v] == False and dist[v] > dist[u] + self.adj[u][v]:
                    dist[v] = dist[u] + self.adj[u][v]

        self.print_solution(dist)



    def print_solution(self, dist):
        print("vertex  Distance from source vertex")

        for node in range(len(self.vertices)):
            

       
            



