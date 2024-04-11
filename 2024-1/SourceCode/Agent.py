import numpy as np

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
     



        