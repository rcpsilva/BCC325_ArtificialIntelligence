from Labirinto import Labirinto
from agents import AgentDFS, AgentGreedy

nlin = 13
ncol = 13

l1 = Labirinto(nlin,ncol,0.25,[0,0],[nlin-1,ncol-1]) 
ag = AgentGreedy(l1)
caminho = ag.act()
print(caminho)