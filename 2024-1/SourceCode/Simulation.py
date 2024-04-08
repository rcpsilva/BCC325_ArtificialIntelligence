from Environment import Maze
from Agent import RandomAgent

start = [0,0]
finish = [3,3]
nrows = 4
ncols = 4
prob = 0.2

maze = Maze(start,finish,nrows,ncols,prob,update_rate=0.05)
ag = RandomAgent(maze)

ag.act()

