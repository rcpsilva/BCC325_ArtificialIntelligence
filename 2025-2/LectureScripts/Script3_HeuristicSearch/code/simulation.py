from agents import AgentDFSMaze, AgentBFSMaze, get_solution
from environments import Maze

matrix = [[0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0]]

matrix = [[0,0,0,0],
          [1,0,1,0],
          [0,0,0,0],
          [0,1,0,1],
          [0,0,0,0]]


maze = Maze(matrix,[0,0],[len(matrix)-1,len(matrix[0])-1])
agent = AgentBFSMaze(maze)

res = agent.search()

print(res.state)

print(get_solution(res))

maze.plot(get_solution(res))