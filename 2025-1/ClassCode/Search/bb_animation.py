import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
from agents import DFBB
from environment import MazeEnvironment

# 1. Definição do labirinto (0=livre, 1=obstáculo, 's' start, 'g' goal)
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

env   = MazeEnvironment(maze)
agent = DFBB(env,21)

# 2. Instrumentar o DFBB para registrar ordem de expansão
visited_order = []
def instrumented_search():
    best_path = None

    while agent.F:
        node = agent.F.pop(-1)
        visited_order.append(node)

        # ao atingir goal, atualiza bound e memoriza melhor nó
        if node == agent.goal:
            cost = agent.visited[node]['c']
            if cost < agent.bound:
                agent.bound = cost
                best_path = node

        # expande vizinhos apenas se g+h < bound
        for v in env.get_neighbors(node):
            g2 = agent.visited[node]['c'] + 1
            if g2 + agent.h(v) < agent.bound:
                if v not in agent.visited or g2 < agent.visited[v]['c']:
                    agent.F.append(v)
                    agent.visited[v] = {'parent': node, 'c': g2}

    return best_path

# substitui e executa
agent.search = instrumented_search
goal = agent.search()
path = agent.get_path(goal)
print(f'Path cost = {len(path)}')

# 3. Construir matriz para visualização
maze_array = np.zeros((len(maze), len(maze[0])), dtype=int)
for i, row in enumerate(maze):
    for j, val in enumerate(row):
        if val == 1:
            maze_array[i, j] = 1

# 4. Setup do plot/colormap
cmap = ListedColormap(['white', 'black', 'deepskyblue', 'limegreen'])
fig, ax = plt.subplots()
im = ax.imshow(maze_array, cmap=cmap, vmin=0, vmax=3)

def update(frame):
    # frames 0..len(visited_order)-1 → nós expandidos
    if frame < len(visited_order):
        r, c = visited_order[frame]
        if maze_array[r, c] == 0:
            maze_array[r, c] = 2
    # frames seguintes → melhor caminho
    else:
        idx = frame - len(visited_order)
        if idx < len(path):
            r, c = path[idx]
            if maze_array[r, c] in (0, 2):
                maze_array[r, c] = 3

    im.set_array(maze_array)
    return [im]

# 5. Legenda e animação
legend_elems = [
    Patch(facecolor='white',      edgecolor='black', label='Espaço livre'),
    Patch(facecolor='black',      edgecolor='black', label='Obstáculo'),
    Patch(facecolor='deepskyblue',edgecolor='black', label='Nós expandidos'),
    Patch(facecolor='limegreen',  edgecolor='black', label='Melhor caminho'),
]
ax.legend(handles=legend_elems, loc='upper left', bbox_to_anchor=(1.05,1))
ax.set_title("DFBB: Depth-First Branch & Bound")
ax.axis('off')

ani = animation.FuncAnimation(
    fig, update,
    frames=len(visited_order) + len(path),
    interval=200, blit=True, repeat=False
)
plt.tight_layout()
plt.show()
