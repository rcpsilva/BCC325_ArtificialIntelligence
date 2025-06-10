import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from agents import DFS
from environment import MazeEnvironment

# Definição do labirinto (0=livre, 1=obstáculo, 's' start, 'g' goal)
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

env = MazeEnvironment(maze)
agent = DFS(env)

# Instrumentar DFS para registrar ordem de expansão
visited_order = []
def instrumented_search():
    while agent.F:
        node = agent.F.pop(-1)          # pop do topo da pilha
        visited_order.append(node)
        if node == agent.goal:
            return agent.goal
        for v in env.get_neighbors(node):
            if v not in agent.visited:
                agent.visited[v] = node
                agent.F.append(v)

agent.search = instrumented_search
goal = agent.search()
path = agent.get_path(goal)

# Montar matriz de visualização (0 livre, 1 obstáculo)
maze_array = np.zeros((len(maze), len(maze[0])), dtype=int)
for i, row in enumerate(maze):
    for j, val in enumerate(row):
        if val == 1:
            maze_array[i,j] = 1

# Colormap: 0=white,1=black,2=deepskyblue,3=limegreen
cmap = ListedColormap(['white','black','deepskyblue','limegreen'])

fig, ax = plt.subplots()
im = ax.imshow(maze_array, cmap=cmap, vmin=0, vmax=3)

def update(frame):
    if frame < len(visited_order):
        r,c = visited_order[frame]
        if maze_array[r,c] == 0:
            maze_array[r,c] = 2
    else:
        idx = frame - len(visited_order)
        if idx < len(path):
            r,c = path[idx]
            if maze_array[r,c] in [0,2]:
                maze_array[r,c] = 3
    im.set_array(maze_array)
    return [im]

legend_elems = [
    Patch(facecolor='white', edgecolor='black', label='Espaço livre'),
    Patch(facecolor='black', edgecolor='black', label='Obstáculo'),
    Patch(facecolor='deepskyblue', edgecolor='black', label='Nós expandidos'),
    Patch(facecolor='limegreen', edgecolor='black', label='Caminho final'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(1.05,1))
plt.title("DFS: Expansão de Nós e Caminho")
plt.axis('off')

ani = animation.FuncAnimation(
    fig, update,
    frames=len(visited_order)+len(path),
    interval=200, blit=True, repeat=False
)
plt.tight_layout()
plt.show()
