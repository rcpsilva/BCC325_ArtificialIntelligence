import numpy as np
import matplotlib.pyplot as plt

class Maze():

    def __init__(self,nrow,ncol,start,exit,pobs=.3,pause=1):

        self.map = np.zeros((nrow,ncol))
        self.start = np.array(start)
        self.exit = np.array(exit)

        #add obstacles

        for i in range(self.map.shape[0]):
            for j in range(self.map.shape[1]):
                if np.random.rand() < pobs and ([i,j]!=self.start).any() and ([i,j]!=self.exit).any():
                    self.map[i][j] = 1

        ################## visualization ###################
        self.map[start[0]][start[1]] = 0.8 
        self.map[exit[0]][exit[1]] = 0.3
        self.pause = pause
        plt.ion()
        self.vis_map()
        plt.draw()
        plt.pause(pause)
        plt.clf()
        ###################################################
                   
    def initial_percepts(self):

        return {'pos':self.start,
                'exit':self.exit,
                'neighbors':self.get_neighbors(self.start),
                'path':[]}
    
    def get_neighbors(self,pos):

        directions = np.array([[1,0],[-1,0],[0,1],[0,-1]])
        candidates = [pos + dir for dir in directions]
        neighbors = [c for c in candidates if (c[0]>=0 and c[0]<=self.map.shape[0]) and (c[1]>=0 and c[1]<=self.map.shape[1]) and (self.map[c[0]][c[1]] !=1)]

        return neighbors
    
    def state_transition(self,action):

        ################## visualization ###################
        plt.ion()
        self.plot_path(action['path'],self.pause)
        ####################################################

        return {'pos': action['move_to'],
                'exit':self.exit,
                'neighbors':self.get_neighbors(action['move_to']),
                'path':action['path']}
    
    # Visualization functions ###############################
    def plot_path(self, path, pause_time):
        plt.axes().invert_yaxis()
        plt.pcolormesh(self.map)
        for i in range(len(path)-1):
            plt.plot([path[i][1]+0.5,path[i+1][1]+0.5],[path[i][0]+0.5,path[i+1][0]+0.5],'-rs')
        plt.draw()
        plt.pause(pause_time)
        plt.clf()

    def vis_map(self):
        plt.axes().invert_yaxis()
        plt.pcolormesh(self.map)
        plt.plot(self.start[1]+0.5, self.start[0]+0.5,'rs')
        plt.show()
    ##########################################################



if __name__ == '__main__':

    nrow = 5
    ncol = 5
    env = Maze(nrow,ncol,[0,0],[nrow-1,ncol-1])

    print(env.map)

    actions = []
    actions.append({'move_to':[0,0],
              'path':[[0,0],[0,1],[0,2],[0,3],[1,3],[2,3]]})
    actions.append({'move_to':[0,0],
              'path':[[0,0],[1,1],[2,2],[3,3]]})
    actions.append({'move_to':[0,0],
              'path':[[0,0],[1,0],[2,0],[3,0]]})
    
    for a in actions:
        env.state_transition(a)