import numpy as np
import matplotlib.pyplot as plt

class AgentDFS:
    def __init__(self, ambiente) -> None:
        self.ambiente = ambiente
        self.percepcoes = ambiente.percepcoes_iniciais()
        self.F = [[self.percepcoes['posicao']]]
        self.C = []
        self.H = []
        self.C_H = []

    def act(self):

        # Executar ação
        # Coletar novas percepções

        plt.ion()
        while self.F:
            path = self.F.pop(-1)
            
            action = {'mover_para':path[-1]}

            ################ VIS ###########
            plotar_caminho(self.ambiente,path,0.001)
            ################################

            self.percepcoes = self.ambiente.muda_estado(action) 

            if (self.percepcoes['posicao'] == self.percepcoes['saida']).all():
                ################ VIS ###########
                plotar_caminho(self.ambiente,path,3)
                ################################
                return path
            else:
                for vi in self.percepcoes['vizinhos']:
                    forma_ciclo = False
                    for no in path:
                        if (no == vi).all():
                            forma_ciclo = True

                    if not forma_ciclo:
                        self.F.append(path + [vi])
        
class AgentEsperto:
    def __init__(self, ambiente, type='Greedy') -> None:
        self.ambiente = ambiente
        self.percepcoes = ambiente.percepcoes_iniciais()
        self.type = type
        self.F = [[self.percepcoes['posicao']]]
        self.C = [cost([self.percepcoes['posicao']])]
        self.H = [heuristica(self.percepcoes['posicao'],self.percepcoes['saida'])]
        self.C_H = [self.C[-1]+self.H[-1]]

    def act(self):

        # Executar ação
        # Coletar novas percepções

        plt.ion()
        while self.F:
            
            if self.type == 'Greedy':
                posicao_na_fronteira = np.argmin(self.H)
            elif self.type == 'LowestCost':
                posicao_na_fronteira = np.argmin(self.C)
            elif self.type == 'AStar':
                posicao_na_fronteira = np.argmin(self.C_H)

            path = self.F.pop(posicao_na_fronteira)
            self.H.pop(posicao_na_fronteira)
            self.C.pop(posicao_na_fronteira)
            self.C_H.pop(posicao_na_fronteira) 
            
            action = {'mover_para':path[-1]}

            ################ VIS ###########
            plotar_caminho(self.ambiente,path,0.001)
            ################################

            self.percepcoes = self.ambiente.muda_estado(action) 

            if (self.percepcoes['posicao'] == self.percepcoes['saida']).all():
                ################ VIS ###########
                plotar_caminho(self.ambiente,path,4)
                ################################
                return path
            else:
                for vi in self.percepcoes['vizinhos']:
                    forma_ciclo = False
                    for no in path:
                        if (no == vi).all():
                            forma_ciclo = True

                    if not forma_ciclo:
                        self.F.append(path + [vi])
                        self.H.append(heuristica(vi,self.percepcoes['saida']))
                        self.C.append(cost(path + [vi]))
                        self.C_H.append(self.H[-1] + self.C[-1])

def cost(path):
    return len(path)-1

def heuristica(no, objetivo):
    manhattan_distance = np.sum(np.abs(no-objetivo))
    return manhattan_distance


def plotar_caminho(ambiente, caminho, tempo):
    plt.axes().invert_yaxis()
    plt.pcolormesh(ambiente.map)
    for i in range(len(caminho)-1):
        plt.plot([caminho[i][1]+0.5,caminho[i+1][1]+0.5],[caminho[i][0]+0.5,caminho[i+1][0]+0.5],'-rs')
    plt.draw()
    plt.pause(tempo)
    plt.clf()


           

