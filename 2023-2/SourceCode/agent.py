from environment import Maze
import numpy as np

class SearchAgent():
    def __init__(self,env,selec_fn,add_fn):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['pos']]]
        self.select_fn = selec_fn
        self.add_fn = add_fn
        self.visited = []

    def act(self):
        
        while(self.F):
            path = self.select_fn(self.F)

            action = {'path': path, 'move_to': path[-1]}

            self.percepts = self.env.state_transition(action)
            
            self.visited.append(path[-1])
            
            if (path[-1] == self.percepts['exit']).all():
                return path
            
            for n in self.percepts['neighbors']:
                if not(any(np.array_equal(n,p) for p in path)) and not(any(np.array_equal(n,p) for p in self.visited)) :
                    self.add_fn(self.F, path, n)
        
        return None

def dfs_select(F):
    return F.pop(-1)

def dfs_add(F,path,n):
    F.append(path+[n]) 

def bfs_select(F):
    return F.pop(0)

def bfs_add(F,path,n):
    F.append(path+[n])


if __name__ == '__main__':
    nrow = 10
    ncol = 10
    env = Maze(nrow,ncol,[0,0],[nrow-1,ncol-1],pobs=0.2)

    ag = SearchAgent(env,bfs_select,bfs_add)

    ag.act()


