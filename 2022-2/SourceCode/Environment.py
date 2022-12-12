import numpy as np
import matplotlib.pyplot as plt

class Environment:

    def __init__(self, rows, cols, start, goal) -> None:
        #Empty map
        self.map = np.zeros((rows,cols))
        
        # Add obstacles
        for i in range(rows):
            for j in range(cols):
                if np.random.random() < .3:
                    self.map[i][j] = 1
       
        x,y = start
        self.map[x][y] = 0

        self.start = start
        self.goal = goal

    def see_map(self):

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j] == 1:
                    plt.plot(i,j,'s')

        plt.grid(True)
        plt.show()

    def get_neighbors(self,position):
        neighbors = []
        n,m = self.map.shape
        r,c = position
        if r+1 >= 0 and r+1 < n:
            if self.map[r+1][c] == 0:
                neighbors.append([r+1,c])
        if r-1 >= 0 and r-1 < n:
            if self.map[r-1][c] == 0:
                neighbors.append([r-1,c])
        if c+1 >= 0 and c+1 < m:
            if self.map[r][c+1] == 0:
                neighbors.append([r,c+1])
        if c-1 >= 0 and c-1 < m:
            if self.map[r][c-1] == 0:
                neighbors.append([r,c-1])

        return neighbors

    def initial_percepts(self):
        return {'goal':self.goal,
                'podsition':self.start,
                'neighbors':self.get_neighbors(self.start)}

    def change_state(self,action):
        return {'goal':self.goal,
                'position':action['position'],
                'neighbors':self.get_neighbors(action['position'])}

if __name__ == '__main__':

    e1 = Environment(5,5,[2,2],[4,4])

    print(e1.map)

    percepts = e1.initial_percepts()
    print(percepts)
    print(percepts['neighbors'])
    print(percepts['neighbors'][0])

    a = {'position':percepts['neighbors'][0]}
    percepts = e1.change_state(a)
    print(percepts)


    
    

        
    

