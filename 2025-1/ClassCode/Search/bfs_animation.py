import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from agents import BFS
from environment import MazeEnvironment

# Labirinto (apenas 0, 1, 's', 'g')
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
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
]

env = MazeEnvironment(maze)
agent = BFS(env)

# Instrumentar busca para registrar a ordem de expansão
visited_order = []
def instrumented_search():
    while agent.F:
        node = agent.F.pop(0)
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

# Construir matriz base: 0=livre, 1=obstáculo
maze_array = np.zeros((len(maze), len(maze[0])), dtype=int)
for i, row in enumerate(maze):
    for j, val in enumerate(row):
        if val == 1:
            maze_array[i, j] = 1

# Definir colormap
cmap = ListedColormap(['white', 'black', 'deepskyblue', 'limegreen'])

# Iniciar figura
fig, ax = plt.subplots()
# <-- AQUI está o truque: vmin=0, vmax=3
im = ax.imshow(maze_array, cmap=cmap, vmin=0, vmax=3)

def update(frame):
    if frame < len(visited_order):
        r, c = visited_order[frame]
        if maze_array[r, c] == 0:
            maze_array[r, c] = 2
    elif frame < len(visited_order) + len(path):
        r, c = path[frame - len(visited_order)]
        if maze_array[r, c] in [0, 2]:
            maze_array[r, c] = 3
    im.set_array(maze_array)
    return [im]

# Legenda
legend_elements = [
    Patch(facecolor='white', edgecolor='black', label='Espaço livre'),
    Patch(facecolor='black', edgecolor='black', label='Obstáculo'),
    Patch(facecolor='deepskyblue', edgecolor='black', label='Nós expandidos'),
    Patch(facecolor='limegreen', edgecolor='black', label='Caminho final')
]
ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(1.05, 1.0))

plt.title("Expansão de Nós com BFS")
plt.axis('off')
ani = animation.FuncAnimation(
    fig, update,
    frames=len(visited_order) + len(path),
    interval=200, blit=True, repeat=False
)
plt.tight_layout()
plt.show()
