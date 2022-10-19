class MazeAgent():

    def __init__(self,env):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['position']]]

    def act(self):

        while self.F:
            path = self.F.pop(0)

            self.percepts = self.env.change_state({'path':path.copy()})

            if self.percepts['goal']:
                break
            else:
                for n in self.percepts['available_neighbors']:
                    self.F.insert(-1,path + [n])
                    
        self.env.draw_best(path)