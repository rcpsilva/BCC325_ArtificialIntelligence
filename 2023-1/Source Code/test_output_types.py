from Labirinto import Labirinto
from agents import AgentDFS, AgentGreedy

class Test_output_types:

    def test_greedy(self):

        nlin = 10
        ncol = 10

        l1 = Labirinto(nlin,ncol,0,[0,0],[nlin-1,ncol-1]) 
        ag = AgentGreedy(l1)
        caminho = ag.act()

        assert type(caminho)==list

    def test_dfs(self):

        nlin = 10
        ncol = 10

        l1 = Labirinto(nlin,ncol,0,[0,0],[nlin-1,ncol-1]) 
        ag = AgentDFS(l1)
        caminho = ag.act()

        assert type(caminho)==list


