import numpy as np
import heapq as hp
from maze import Maze

def heuristic(node, goal):
    return np.linalg.norm(np.array(node) - np.array(goal),1)

def cost(node1, node2):
    return np.linalg.norm(np.array(node1) - np.array(node2),1)

def cost(path):

    cost = 0
    for i in range(len(path)-1):
        cost += np.linalg.norm(np.array(path[i]) - np.array(path[i+1]),1)

    return cost

class MazeAgentAStar():

    def __init__(self,env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = []
        hp.heappush(self.F,(cost([self.percepts['position']]) + heuristic(self.percepts['position'],self.percepts['goal_position']),[self.percepts['position']]))

    def act(self):

        while self.F:
            path = hp.heappop(self.F)[1]

            self.percepts = self.env.change_state({'path':path.copy()})

            if self.percepts['goal']:
                break

            for n in self.percepts['available_neighbors']:
                if n not in path:
                    hp.heappush(self.F,(cost(path + [n]) + heuristic(n, self.percepts['goal_position']),path + [n]))

        self.env.draw_best(path)

class MazeAgentDFS():

    def __init__(self,env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]

    def act(self):

        while self.F:
            path = self.F.pop(-1)

            self.percepts = self.env.change_state({'path':path.copy()})

            if self.percepts['goal']:
                break

            for n in self.percepts['available_neighbors']:
                if n not in path:
                    self.F.insert(-1, path + [n])

        self.env.draw_best(path)

class MazeAgentBB():

    def __init__(self,env,bound):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]
        self.best_path = []
        self.bound = bound

    def act(self):

        while self.F:
            path = self.F.pop(-1)

            self.percepts = self.env.change_state({'path':path.copy()})

            if self.percepts['goal']:
                if cost(path) < self.bound:
                    self.bound = cost(path)
                    self.best_path = path
                
            for n in self.percepts['available_neighbors']:
                if n not in path:
                    if (cost(path + [n]) + heuristic(n,self.percepts['goal']) < self.bound):
                        self.F.insert(-1, path + [n])

        self.env.draw_best(self.best_path)


if __name__ == '__main__':

    env = Maze(5,5)

    percepts = env.initial_percepts()

    print(percepts['position'])
    print(percepts['goal'])
    print(percepts['available_neighbors'])
    print(percepts['goal_position'])
    


    
