import numpy as np

class RandomAgent():

    def __init__(self,env):

        self.percepts = env.initial_stimuli()
        self.F = [[self.percepts['pos']]]
        self.env = env

    def act(self):
        
        while self.F:

            path = self.F.pop(np.random.randint(0,len(self.F)))

            action = {'to_visit':path[-1]}

            self.percepts = self.env.react(action)

            if all(path[-1] == self.percepts['finish']):
                return path
            
            for n in self.percepts['neighbors']:
                self.F.append(path + [n])



     



        