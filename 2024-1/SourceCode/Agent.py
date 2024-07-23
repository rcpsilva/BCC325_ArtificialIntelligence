import numpy as np
import heapq
from copy import copy, deepcopy

class RandomAgent():

    def __init__(self,env):

        self.percepts = env.initial_stimuli()
        self.F = [[self.percepts['pos']]]
        self.env = env

    def act(self):
        
        while self.F:

            path = self.F.pop(np.random.randint(0,len(self.F)))

            action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':False}

            self.percepts = self.env.react(action)

            if all(path[-1] == self.percepts['finish']):
                action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':True}
                self.percepts = self.env.react(action)
                return path
            
            for n in self.percepts['neighbors']:
                self.F.append(path + [n])

class DFSAgent():

    def __init__(self,env):

        self.percepts = env.initial_stimuli()
        self.F = [[self.percepts['pos']]]
        self.env = env

    def act(self):
        
        while self.F:

            path = self.F.pop(-1)

            action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':False}

            self.percepts = self.env.react(action)

            if all(path[-1] == self.percepts['finish']):
                action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':True}
                self.percepts = self.env.react(action)
                return path
            
            for n in self.percepts['neighbors']:
                cycle = False
                for node in path:
                    if n[0]==node[0] and n[1]==node[1]:
                        cycle = True
                if not cycle:
                    self.F.append(path + [n])
                    
class BFSAgent():

    def __init__(self,env):

        self.percepts = env.initial_stimuli()
        self.F = [[self.percepts['pos']]]
        self.env = env

    def act(self):
        
        while self.F:

            path = self.F.pop(0)

            action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':False}

            self.percepts = self.env.react(action)

            if all(path[-1] == self.percepts['finish']):
                action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':True}
                self.percepts = self.env.react(action)
                return path
            
            for n in self.percepts['neighbors']:
                cycle = False
                for node in path:
                    if n[0]==node[0] and n[1]==node[1]:
                        cycle = True
                if not cycle:
                    self.F.append(path + [n])
     
def cost(path, map):
    cost = 0
    for node in path:
        cost += map[node[0]][node[1]]

    return cost

def h(node, goal):

    return (abs(node[0]-goal[0]) + abs(node[1]-goal[1]))*0.3

class LCFAgent():

    def __init__(self,env):

        self.percepts = env.initial_stimuli()
        self.F = []
        heapq.heappush(self.F,(0,np.random.rand(),[self.percepts['pos']]))
        self.env = env

    def act(self):
        
        while self.F:

            path = heapq.heappop(self.F)[2]
            
            action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':False}

            self.percepts = self.env.react(action)

            if all(path[-1] == self.percepts['finish']):
                action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':True}
                self.percepts = self.env.react(action)
                return path
            
            for n in self.percepts['neighbors']:
                cycle = False
                for node in path:
                    if n[0]==node[0] and n[1]==node[1]:
                        cycle = True
                if not cycle:
                    c = cost(path+[n],self.env.map)
                    heapq.heappush(self.F,(c,np.random.rand(),path + [n]))

class AStarAgent():

    def __init__(self,env):

        self.percepts = env.initial_stimuli()
        self.F = []
        heapq.heappush(self.F,(0+h(self.percepts['pos'],self.percepts['finish']),np.random.rand(),[self.percepts['pos']]))
        self.env = env

    def act(self):
        
        while self.F:

            path = heapq.heappop(self.F)[2]
            
            action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':False}

            self.percepts = self.env.react(action)

            if all(path[-1] == self.percepts['finish']):
                action = {'to_visit':path[-1],
                      'path':path,
                      'freeze':True}
                self.percepts = self.env.react(action)
                return path
            
            for n in self.percepts['neighbors']:
                cycle = False
                for node in path:
                    if n[0]==node[0] and n[1]==node[1]:
                        cycle = True
                if not cycle:
                    c = cost(path+[n],self.env.map)
                    heu = h(self.percepts['pos'],self.percepts['finish'])
                    heapq.heappush(self.F,(c+heu,np.random.rand(),path + [n]))

class BBAgent():

    def __init__(self,env,bound=10000):

        self.percepts = env.initial_stimuli()
        self.F = [[self.percepts['pos']]]
        self.env = env
        self.bound = bound
        self.best_cost = bound
        self.best_path = []

    def act(self):
        
        while self.F:

            path = self.F.pop(-1)

            if (cost(path,self.env.map) + h(path[-1],self.percepts['finish'])) < self.bound:


                action = {'to_visit':path[-1],
                        'path':path,
                        'freeze':False}

                self.percepts = self.env.react(action)

                if all(path[-1] == self.percepts['finish']):
                    action = {'to_visit':path[-1],
                        'path':path,
                        'freeze':False}
                    self.percepts = self.env.react(action)
                    c = cost(path,self.env.map) 
                    if c < self.best_cost:
                        self.best_cost = c
                        self.best_path = copy(path)
                        self.bound = c                

                for n in self.percepts['neighbors']:
                    cycle = False
                    for node in path:
                        if n[0]==node[0] and n[1]==node[1]:
                            cycle = True
                    if not cycle:
                        self.F.append(path + [n])

        return self.best_path
    
   