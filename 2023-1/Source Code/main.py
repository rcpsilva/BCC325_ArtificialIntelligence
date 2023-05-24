from Labirinto import Labirinto
from agents import AgentDFS

nlin = 7
ncol = 7

l1 = Labirinto(nlin,ncol,0.25,[0,0],[nlin-1,ncol-1]) 

ag = AgentDFS(l1)
caminho = ag.act()
print(caminho)