import numpy as np

class Maze():

    def __init__(self,nrow,ncol,start,exit,pobs=.3):

        self.map = np.zeros((nrow,ncol))
        self.start = np.array(start)
        self.exit = np.array(exit)

        #add obstacles

        for i in range(self.map.shape[0]):
            for j in range(self.map.shape[1]):
                if np.random.rand() < pobs and ([i,j]!=self.start).any() and ([i,j]!=self.exit).any():
                    self.map[i][j] = 1

                   
    def initial_percepts(self):

        return {'pos':self.start,
                'exit':self.exit,
                'neighbors':self.get_neighbors(self.start)}
    
    def get_neighbors(self,pos):

        directions = np.array([[1,0],[-1,0],[0,1],[0,-1]])
        candidates = [pos + dir for dir in directions]
        neighbors = [c for c in candidates if (c[0]>=0 and c[0]<=self.map.shape[0]) and (c[1]>=0 and c[1]<=self.map.shape[1]) and (self.map[c[0]][c[1]] !=1)]

        return neighbors
    
    def state_transition(self,action):

        return {'pos': action['move_to'],
                'exit':self.exit,
                'neighbors':self.get_neighbors(action['move_to'])}

if __name__ == '__main__':

    nrow = 5
    ncol = 5
    env = Maze(nrow,ncol,[0,0],[nrow-1,ncol-1])

    print(env.map)

    print(env.initial_percepts())

    print(env.get_neighbors(np.array([1,2])))
    print(env.get_neighbors(np.array([1,1])))
    print(env.get_neighbors(np.array([3,3])))
    print(env.get_neighbors(np.array([2,2])))