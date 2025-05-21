from agents import BFS, DFS
from environment import MazeEnvironment

maze = [
    ['s', 0,   1,   0,   0],
    [ 1 , 0,   1,   0,   1],
    [ 0 , 0,   0,   0,  'g']
]

print("Labirinto original:")
for row in maze:
    print(row)

# Cria o ambiente a partir do labirinto
env = MazeEnvironment(maze)

print(env.pos_start)
print(env.pos_goal)

# Executa BFS
#agent = BFS(env)
#goal = agent.search()
#path = agent.get_path(goal)

#print("\nCaminho encontrado (BFS):")
#print(path)

# Imprime o labirinto com o caminho marcado com "*"
#maze_with_path = [row.copy() for row in maze]
#for i, (r, c) in enumerate(path):
#    if maze_with_path[r][c] not in ['s', 'g']:
#        maze_with_path[r][c] = '*'

#print("\nLabirinto com o caminho:")
#for row in maze_with_path:
#    print(row)
