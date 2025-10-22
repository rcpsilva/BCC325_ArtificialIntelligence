from environment import Maze
from agent import *
import numpy as np

matrix = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]

matrix = [[0,1,1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,1,0,1,0,0],
          [1,1,0,0,0,1,0,1,0,0],
          [0,0,0,0,0,0,0,1,0,0],
          [0,0,0,1,0,0,0,1,1,0],
          [0,0,0,1,0,0,0,0,1,1],
          [0,0,0,1,0,0,0,0,0,0]]

env = Maze(matrix,np.array([0,0]),[len(matrix)-1,len(matrix[0])-1])

bfs = AgentMaze(env, add_last, remove_first, lambda s,s_: 0.0, lambda s,G: 0.0)

res = bfs.search()

print(res)
print(res.depth)

env.plot(get_solution(res))