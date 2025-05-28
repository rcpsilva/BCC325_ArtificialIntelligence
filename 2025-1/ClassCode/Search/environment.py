class MazeEnvironment:
    def __init__(self,maze):

        self.start, self.goal= self.pos_start_goal(maze)
        self.maze = maze

    def pos_start_goal(self, maze):
        start = None
        goal = None
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'g':
                    goal = (i,j)
                if maze[i][j] == 's':
                    start = (i,j)

        return start, goal

    def get_neighbors(self,pos):

        actions = [(pos[0],pos[1]+1),(pos[0],pos[1]-1),(pos[0]+1,pos[1]),(pos[0]-1,pos[1])]
        neighbors = []

        for action in actions:
            # se está dentro do tabuleiro

            if (0 <= action[0] < len(self.maze)) and (0 <= action[1] < len(self.maze[0])):
                # se é um posição livre
                if self.maze[action[0]][action[1]] != 1:
                    neighbors.append(action)

        return neighbors


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




        


       