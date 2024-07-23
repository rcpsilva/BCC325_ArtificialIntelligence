from Environment import Maze
from Agent import RandomAgent,DFSAgent,BFSAgent,LCFAgent,BBAgent,AStarAgent

start = [0,0]
finish = [7,7]
nrows = 8
ncols = 8
prob = 0.0

maze = Maze(start,finish,nrows,ncols,prob,update_rate=0.05)
ag = LCFAgent(maze)

ag.act()

