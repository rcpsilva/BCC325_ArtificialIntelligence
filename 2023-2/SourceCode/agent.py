from environment import Maze
import numpy as np

class IDAgent():
    def __init__(self,env,selec_fn,add_fn):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['pos']]]
        self.select_fn = selec_fn
        self.add_fn = add_fn
        self.visited = [self.percepts['pos']]

    def act(self):
        height_bound = 0
        bound_violation = True

        while bound_violation:
            bound_violation = False
            height_bound+=1
            self.percepts = env.initial_percepts()
            self.visited = [self.percepts['pos']]
            self.F = [[self.percepts['pos']]]
            while(self.F):
                path = self.select_fn(self.F)
                action = {'path': path, 'move_to': path[-1]}

                self.percepts = self.env.state_transition(action)
                
                if (path[-1] == self.percepts['exit']).all():
                    return path
                
                if len(path) + 1 <= height_bound:
                    for n in self.percepts['neighbors']:
                        if not(any(np.array_equal(n,p) for p in path)) and not(any(np.array_equal(n,p) for p in self.visited)) :
                            self.add_fn(self.F, path, n)
                            self.visited.append(n)
                else:
                    bound_violation = True
                
        return None


class SearchAgent():
    def __init__(self,env,selec_fn,add_fn):
        self.env = env
        self.percepts = env.initial_percepts()
        self.F = [[self.percepts['pos']]]
        s = self.percepts['pos'] # starting position
        self.C = [env.map[s[0]][s[1]]]
        self.select_fn = selec_fn
        self.add_fn = add_fn
        self.visited = [self.percepts['pos']]

    def act(self):
        
        while(self.F):
            path = self.select_fn(self.F)
            c = self.select_fn(self.C) 

            action = {'path': path, 'move_to': path[-1]}

            self.percepts = self.env.state_transition(action)
            
            if (path[-1] == self.percepts['exit']).all():
                return path, c
            
            for n,cn in zip(self.percepts['neighbors'],self.percepts['neighbors_cost']):
                if not(any(np.array_equal(n,p) for p in path)) and not(any(np.array_equal(n,p) for p in self.visited)) :
                    self.add_fn(self.F, path, [n])
                    self.add_fn(self.C, c, cn)
                    self.visited.append(n)
        
        return None,None

def dfs_select(F):
    return F.pop(-1)

def dfs_add(F,path,n):
    F.append(path+n) 

def bfs_select(F):
    return F.pop(0)

def bfs_add(F,path,n):
    F.append(path+n)


if __name__ == '__main__':
    nrow = 15
    ncol = 15
    env = Maze(nrow,ncol,[0,0],[nrow-1,ncol-1],pobs=0.2)

    ag = SearchAgent(env,dfs_select,dfs_add)
    #ag = IDAgent(env,dfs_select,dfs_add)

    path, cost = ag.act()

    print(path)
    print(f'Cost: {cost}')


