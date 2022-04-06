from queue import PriorityQueue

class Graph:

    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.edges = [[-1 for _ in range(vertices_count)] for _ in range(vertices_count)]
        self.visited = [False for _ in range(vertices_count)]
    
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    

    def dijkstra(self, start_vertex):
        distances = {v: float('inf') for v in range(self.vertices_count)}
        distances[start_vertex] = 0
        visited = [False for _ in range(self.vertices_count)]
        pq = PriorityQueue()
        pq.put(start_vertex)

        while not pq.empty():
            current_vertex = pq.get()
            visited[current_vertex] = True

            for neighbor in range(self.vertices_count):
                distance = self.edges[current_vertex][neighbor]
                if distance == -1:
                    continue

                if visited[neighbor]:
                    continue
            
                old_cost = distances[neighbor]
                new_cost = distances[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put(neighbor)
                    distances[neighbor] = new_cost

        return distances       


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 6, 7)
g.add_edge(1, 6, 11)
g.add_edge(1, 7, 20)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 6)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 10)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 15)
g.add_edge(4, 7, 1)
g.add_edge(4, 8, 5)
g.add_edge(5, 8, 12)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 3)
D = g.dijkstra(0)
print(D)
"""
{0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11}

{0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11}


"""
