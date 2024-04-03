import numpy as np

class Maze():

    def __init__(self, start, finish, nrows, ncols, prob):
        
        self.start = np.array(start)
        self.finish = np.array(finish)
        self.map = np.random.random((nrows,ncols))
        self.directions = np.array([[0,1],[0,-1],[1,0],[-1,0]])
        self.nrows = nrows
        self.ncols = ncols

        for i in range(self.map.shape[0]):
            for j in range(self.map.shape[1]):
                if (i != start[0] or j!=start[1]) and (i != finish[0] or j!=finish[1]):
                    if np.random.random() < prob:
                        self.map[i][j] = 1  

    def get_neighbors(self,pos):

        neighbors = []
        costs = []
        
        for d in self.directions:
            candidate = pos+d
            if (self.map[candidate[0]][candidate[1]] != 1) and (0 <= candidate[0] < self.nrows) and (0 <= candidate[1] < self.ncols): 
                neighbors.append(candidate)
                costs.append(self.map[candidate[0]][candidate[1]])

        return neighbors,costs

    
    def initial_stimuli(self):

        neighbors, costs = self.get_neighbors(self.start)

        return {'pos':self.start,
                'neighbors': neighbors,
                'neighbors_costs': costs}
    
    def react(self,action):

        pos = action['to_visit']

        neighbors, costs = self.get_neighbors(pos)

        return {'pos':pos,
                'neighbors': neighbors,
                'neighbors_costs': costs}



