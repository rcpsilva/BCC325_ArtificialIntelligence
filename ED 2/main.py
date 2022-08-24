from pyamaze import maze,COLOR,agent
from maze import Maze
from maze_agent import MazeAgentDFS,MazeAgentAStar,MazeAgentBB

env = Maze(10,10)
#ag = MazeAgentDFS(env)
ag = MazeAgentAStar(env)
#ag = MazeAgentBB(env,40)
#ag = MazeAgentDFS(env)
ag.act()