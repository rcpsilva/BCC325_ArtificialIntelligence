import math
class AStar():

    def __init__(self,env):

        self.env = env
        self.goal = env.goal
        self.visited = {env.start:{'parent':-1,'c':0}}
        self.F = [env.start]

    def h(self, pos):
        # Manhattan Distance
        return (abs(pos[0]-self.goal[0]) + abs(pos[1]-self.goal[1]))

    def c(self,pos):
        return self.visited[pos]['c']
    
    def find_min(self, F):

        min_val = math.inf
        min_idx = -1

        for i in range(len(F)):
            node = F[i]
            priority = self.c(node) + self.h(node)
            if priority < min_val:
                min_val = priority
                min_idx = i

        return min_idx

    def search(self):
        while self.F:
            min_idx = self.find_min(self.F)
            node = self.F.pop(min_idx)

            if node==self.goal:
                return self.goal
            
            for v in self.env.get_neighbors(node):
                
                if v not in self.visited:
                    self.F.append(v)
                    self.visited[v] = {'parent':node,'c':self.visited[node]['c']+1}
                else:
                    new_cost = self.visited[node]['c']+1
                    if new_cost < self.visited[v]['c']:
                        self.F.append(v)
                        self.visited[v] = {'parent':node,'c':new_cost}

    def get_path(self,goal):
        node = goal
        path = [node]
        while self.visited[node]['parent'] != -1:
            path.append(self.visited[node]['parent'])
            node = self.visited[node]['parent']

        path.reverse()
        return path


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
    
    