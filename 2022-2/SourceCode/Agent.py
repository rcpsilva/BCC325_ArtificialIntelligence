import math
import heapq

class Agent():
    def __init__(self, env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]

    def h(self,n):
        return math.abs(self.percepts['goal'][0]-n[0]) + math.abs(self.percepts['goal'][1]-n[1])

    def act(self):
        while self.F:
            path = self.F.pop(0)

            action = {'position':path[-1]}
            self.percepts = self.env.change_state(action)

            if path[-1] == self.percepts['goal']:
                return path
            else:
                for n in self.percepts['neighbors']:
                    if n not in path:
                        self.F.append(path + [n])

        print('Impossible!')
        return []

def h(n,percepts):
        return abs(percepts['goal'][0]-n[0]) + abs(percepts['goal'][1]-n[1])

class GreedyAgent():

    def __init__(self, env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = []
        heapq.heappush(self.F,(h(self.percepts['position'],self.percepts),[self.percepts['position']]))

    def act(self):
        while self.F:
            path = heapq.heappop(self.F)[1]
            action = {'position':path[-1]}
            self.percepts = self.env.change_state(action)

            if path[-1] == self.percepts['goal']:
                return path
            else:
                for n in self.percepts['neighbors']:
                    if n not in path:
                        heapq.heappush(self.F,(h(n,self.percepts),path + [n]))
            

        print('Impossible!')
        return []









