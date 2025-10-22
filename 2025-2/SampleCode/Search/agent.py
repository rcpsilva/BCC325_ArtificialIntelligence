import numpy as np

class Node:

    def __init__(self, state, parent=None, g=0.0, h=0.0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.depth = 0 if parent is None else parent.depth + 1

    def __eq__(self, other):
        return np.array_equal(self.state,other.state)
    
    def __hash__(self):
        return hash(self.state.tobytes())
    
    def __str__(self):
        return f'({self.state[0],self.state[1]})'


def get_solution(node):
    solution = []
    solution.append(node.state)

    while node.parent:
        node = node.parent
        solution.append(node.state)

    solution.reverse()
    return solution

def add_last(F,s):
    F.append(s)

def remove_first(F):
    return F.pop(0)

def remove_last(F):
    return F.pop(-1)

class AgentMaze:

    def __init__(self, env, add_fcn, remove_fcn, cost_fcn, h_fcn):
        self.env = env
        self.add_fcn = add_fcn
        self.remove_fcn = remove_fcn
        self.cost_fcn = cost_fcn
        self.h_fcn = h_fcn

        self.G = self.env.initial_percepts()['exit']

        self.visited = set()

    def search(self):

        s0 = Node(self.env.initial_percepts()['start'],
                  None,
                  g=0.0,
                  h=self.h_fcn(self.env.initial_percepts()['start'],
                               self.G))

        F = []

        self.add_fcn(F,s0)

        while F:

            s = self.remove_fcn(F)
            print(s)

            if (s.state == self.G).all():
                return s

            self.visited.add(s)

            for s_ in self.env.get_neighbors(s.state):
                s_node = Node(s_,s,self.cost_fcn(s,s_),self.h_fcn(s_,self.G))
                if s_node not in self.visited:
                    self.add_fcn(F,s_node)

        return None



