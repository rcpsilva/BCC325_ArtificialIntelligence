import numpy as np
import matplotlib.pyplot as plt

class Maze():

    def __init__(self, start, finish, nrows, ncols, prob, update_rate=0.05):
        
        self.start = np.array(start)
        self.finish = np.array(finish)
        self.map = np.random.random((nrows,ncols))*0.7
        self.directions = np.array([[0,1],[0,-1],[1,0],[-1,0]])
        self.nrows = nrows
        self.ncols = ncols
        self.update_rate = update_rate

        for i in range(self.map.shape[0]):
            for j in range(self.map.shape[1]):
                if (i != start[0] or j!=start[1]) and (i != finish[0] or j!=finish[1]):
                    if np.random.random() < prob:
                        self.map[i][j] = 1  

        self.render_environment()

    def get_neighbors(self,pos):

        neighbors = []
        costs = []
        for d in self.directions:
            candidate = pos+d
            if  (0 <= candidate[0] < self.nrows) and (0 <= candidate[1] < self.ncols):
                if (self.map[candidate[0]][candidate[1]] != 1): 
                    neighbors.append(candidate)
                    costs.append(self.map[candidate[0]][candidate[1]])

        return neighbors,costs


    def initial_stimuli(self):

        neighbors, costs = self.get_neighbors(self.start)

        return {'pos':self.start,
                'finish':self.finish,
                'neighbors': neighbors,
                'neighbors_costs': costs}

    def react(self,action):

        pos = action['to_visit']

        self.render_path(action['path'],action['freeze'])

        neighbors, costs = self.get_neighbors(pos)

        return {'pos':pos,
                'finish':self.finish,
                'neighbors': neighbors,
                'neighbors_costs': costs}
    
    def render_environment(self):

        self.map[self.start[0]][self.start[1]] = 0 
        self.map[self.finish[0]][self.finish[1]] = 0
        plt.ion()
        
        plt.axes().invert_yaxis()
        plt.pcolormesh(self.map)
        plt.plot(self.start[1]+0.5, self.start[0]+0.5,'rs')
        plt.show()

        plt.draw()
        plt.pause(self.update_rate)
        plt.clf()

    def render_path(self,path,freeze):

        plt.ion()
        plt.axes().invert_yaxis()
        plt.pcolormesh(self.map)
        for i in range(len(path)-1):
            plt.plot([path[i][1]+0.5,path[i+1][1]+0.5],[path[i][0]+0.5,path[i+1][0]+0.5],'-rs')
        plt.draw()
        if freeze:
            plt.pause(30)
        else:    
            plt.pause(self.update_rate)
            plt.clf()
        
