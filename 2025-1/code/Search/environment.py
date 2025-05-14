
class Environment:
    def __init__(self,G={},start=[],goal=[]):
        if G:
            self.G=G
        else:
            self.G = {'A':['B','C'],
                 'B':['D','E'],
                 'C':['F'],
                 'D':[],
                 'E':[],
                 'F':['G','H'],
                 'G':[],
                 'H':[]}
        if not start:
            self.start = 'A'
        else:
            self.start = start
        
        if not goal:
            self.goal = 'G'
        else:
            self.goal = goal

    def get_neighbors(self,state):
        return self.G[state]

if __name__ == '__main__':

    env = Environment()

    print(env.G)
    print(env.goal)
    print(env.start)

    print(env.get_neighbors('A'))

    print(env.get_neighbors('F'))




        


       