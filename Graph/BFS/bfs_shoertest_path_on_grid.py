from collections import deque



class Graph:

    def __init__(self, maze):

        self.maze = maze
        self.nodes_left_in_layer = 1
        self.nodes_in_next_layer = 0
        self.move_count = 0
        self.column_que = deque()
        self.row_que = deque()
        self.visited = [ [False for i in range(len(self.maze[j]))] for j in range(len(self.maze))]
        

    
    def explore_neighbours(self, r, c):
        

        for direc in ['U', 'D', 'R', 'L']:

            i = 0
            j = 0
            if direc == 'U':
                i = -1
            elif direc == 'D':
                i = 1
            elif direc == 'R':
                j = 1
            elif direc == 'L':
                j = -1
                
            rr = r + i
            cc = c + j

            if rr < 0 or cc < 0: continue
            if rr >= len(self.maze)  or cc >= len(self.maze[0]): continue
            if self.visited[rr][cc]: continue
            if self.maze[rr][cc] == '#':
                print('#')
                continue

            
            self.row_que.append(rr)
            self.column_que.append(cc)
            self.visited[rr][cc] = True
            self.nodes_in_next_layer += 1

            return direc

    def print_maze(self):

        for row in self.maze:
            print(row)


    def shortest_path(self, sr, sc):

        
        self.row_que.append(sr)
        self.column_que.append(sc)

        reached_end = False
        print(self.visited[sr][sc])
        self.visited[sr][sc] = True

        while self.row_que and self.column_que:

            r = self.row_que.popleft()
            c = self.column_que.popleft()

            if self.maze[r][c] == 'E':
                reached_end = True
                break
            
            way = self.explore_neighbours(r, c)
            print(way)
            self.nodes_left_in_layer -= 1 
            if self.nodes_left_in_layer == 0:
                self.nodes_left_in_layer = self.nodes_in_next_layer
                self.nodes_in_next_layer = 0
                self.move_count += 1
                

        if reached_end:
            return move_count
        
        return -1
        
maze = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['.', '.', '#', 'E', '.']
]   


graph = Graph(maze)
print(graph.shortest_path(0, 0))
graph.print_maze()
