import numpy as np

class Node:

    def __init__(self, state, parent=None, g=0.0):
        self.state  = state
        self.parent = parent
        self.g      = g
        self.depth  = 0 if parent is None else parent.depth + 1

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return np.array_equal(self.state, other.state)

    def __hash__(self):
        return hash(self.state.tobytes())
    
def get_solution(node):
    solution = []
    solution.append(list(node.state))
    while node.parent:
        node = node.parent
        solution.append(list(node.state))
    solution.reverse()
    return solution

class AgentDFSMaze:

    def __init__(self, env):
        self.env = env
        self.visited = set()
        self.initial_percepts = env.initial_percepts()
        self.G = self.initial_percepts['exit']

    def search(self):

        s0 = Node(self.initial_percepts['start'])

        if (self.initial_percepts['start'] == self.G).all():
            return s0 
        
        self.visited.add(s0)
        F = [s0]

        while F:

            s = F.pop(-1)
            
            print(s.state)
            
            for s_ in self.env.get_neighbors(s.state):
                s_node = Node(s_,s)
                if s_node not in self.visited:
                    if (s_node.state == self.G).all():
                        return s_node
                    self.visited.add(s_node)
                    F.append(s_node)

        return None
    
class AgentBFSMaze:

    def __init__(self, env):
        self.env = env
        self.visited = set()
        self.initial_percepts = env.initial_percepts()
        self.G = self.initial_percepts['exit']

    def search(self):

        s0 = Node(self.initial_percepts['start'])

        if (self.initial_percepts['start'] == self.G).all():
            return s0 
        
        self.visited.add(s0)
        F = [s0]

        while F:

            s = F.pop(0)
            
            print(s.state)
            
            for s_ in self.env.get_neighbors(s.state):
                s_node = Node(s_,s)
                if s_node not in self.visited:
                    if (s_node.state == self.G).all():
                        return s_node
                    self.visited.add(s_node)
                    F.append(s_node)

        return None




