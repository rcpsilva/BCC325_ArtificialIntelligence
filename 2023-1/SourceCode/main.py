from Labirinto import Labirinto
from agents import AgentDFS, AgentEsperto

nlin = 12
ncol = 12

l1 = Labirinto(nlin,ncol,0.25,[0,0],[nlin-1,ncol-1]) 
ag = AgentEsperto(l1,type='Greedy')
caminho = ag.act()
print(caminho)