from Environment import Maze
from Agent import RandomAgent,DFSAgent,BFSAgent,LCFAgent,BBAgent

start = [0,0]
finish = [9,9]
nrows = 10
ncols = 10
prob = 0.0

maze = Maze(start,finish,nrows,ncols,prob,update_rate=0.05)
ag = BBAgent(maze,10)

ag.act()

