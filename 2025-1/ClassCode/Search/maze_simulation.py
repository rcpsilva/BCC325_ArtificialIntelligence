from agents import BFS, DFS, AStar, DFBB
from environment import MazeEnvironment
  
maze = [
    ['s', 0,   1,   0,   0],
    [ 1 , 0,   1,   0,   1],
    [ 0 , 0,   0,   0,  'g']
]

maze = [
    ['s',0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,'g'],
]

maze = [
    ['s',0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0],
    [0,0,0,1,1,1,1,1,0],
    [0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,1,1],
    [0,0,0,0,0,1,0,0,'g'],
    [0,0,0,0,0,1,0,1,1],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
]

print("Labirinto original:")
for row in maze:
    print(row)

# Cria o ambiente a partir do labirinto
env = MazeEnvironment(maze)

print(env.start)
print(env.goal)

#print(env.get_neighbors((0,0)))
#print(env.get_neighbors((1,1)))
#print(env.get_neighbors((2,3)))


# Executa BFS
agent = BFS(env)
goal = agent.search()
path = agent.get_path(goal)

print("\nCaminho encontrado (BFS):")
print(path)

# Imprime o labirinto com o caminho marcado com "*"
maze_with_path = [row.copy() for row in maze]
for i, (r, c) in enumerate(path):
    if maze_with_path[r][c] not in ['s', 'g']:
        maze_with_path[r][c] = '*'

print("\nLabirinto com o caminho:")
for row in maze_with_path:
    print(row)

print(f'Tamanho do caminho: {len(path)}')