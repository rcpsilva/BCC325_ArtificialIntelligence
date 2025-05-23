class BFS():

    def __init__(self,env):

        self.env = env
        self.goal = env.goal
        self.visited = {env.start:''}
        self.F = [env.start]


    def search(self):
        while self.F:
            node = self.F.pop(0)

            if node==self.goal:
                return self.goal
            
            for v in self.env.get_neighbors(node):
                if v not in self.visited:
                    self.visited[v] = node
                    self.F.append(v)


    def get_path(self,goal):
        node = goal
        path = [node]
        while self.visited[node] != '':
            path.append(self.visited[node])
            node = self.visited[node]

        path.reverse()
        return path
    
class DFS():

    def __init__(self,env):

        self.env = env
        self.goal = env.goal
        self.visited = {env.start:''}
        self.F = [env.start]


    def search(self):
        while self.F:
            node = self.F.pop(-1)

            if node==self.goal:
                return self.goal
            
            for v in self.env.get_neighbors(node):
                
                if v not in self.visited:
                    self.F.append(v)

                self.visited[v] = node

    def get_path(self,goal):
        node = goal
        path = [node]
        while self.visited[node] != '':
            path.append(self.visited[node])
            node = self.visited[node]

        path.reverse()
        return path
    
    