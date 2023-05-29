from Labirinto import Labirinto
from agents import AgentDFS, AgentEsperto

class TestOutTypes:

    def test_esperto(self):

        nlin = 3
        ncol = 3

        l1 = Labirinto(nlin,ncol,0,[0,0],[nlin-1,ncol-1]) 
        ag = AgentEsperto(l1)
        caminho = ag.act()

        assert type(caminho)==list

    def test_dfs(self):

        nlin = 3
        ncol = 3

        l1 = Labirinto(nlin,ncol,0,[0,0],[nlin-1,ncol-1]) 
        ag = AgentDFS(l1)
        caminho = ag.act()

        assert type(caminho)==list

