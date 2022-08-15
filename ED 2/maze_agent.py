import numpy as np
import heapq as hp

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
        hp.heappush(self.F,(heuristic(self.percepts['position'],self.percepts['goal_position']),[self.percepts['position']]))


    def act(self):

        while self.F:
            path = hp.heappop(self.F)[1]

            self.percepts = self.env.change_state({'path':path.copy()})

            if self.percepts['goal']:
                break
            else:
                for n in self.percepts['available_neighbors']:
                    if n not in path:
                        hp.heappush(self.F,(cost(path + [n]) + heuristic(n, self.percepts['goal_position']), path + [n]))
                        

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
            else:
                for n in self.percepts['available_neighbors']:
                    if n not in path:
                        self.F.insert(-1,path + [n])

        self.env.draw_best(path)

if __name__ == '__main__':

    x = [10,10]
    y = [0,0] 

    print(np.linalg.norm(np.array(x) - np.array(y)))
    print(np.linalg.norm(np.array(x) - np.array(y),1))
