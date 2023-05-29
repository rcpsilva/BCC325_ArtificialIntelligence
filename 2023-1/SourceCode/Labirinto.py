import numpy as np
import matplotlib.pyplot as plt

class Labirinto:

    def __init__(self,rows,cols,p_obs,entrada,saida):
        
        self.map = np.zeros((rows,cols))
        self.entrada = np.array(entrada)
        self.saida = np.array(saida)

        # adicionar obstaculus
        for i in range(rows):
            for j in range(cols):
                if np.random.random() < p_obs:
                    self.map[i][j] = 1 

        self.map[entrada[0]][entrada[1]] = 0.8

        self.map[saida[0]][saida[1]] = 0.3
    
    def vis_map(self):

        plt.axes().invert_yaxis()
        plt.pcolormesh(self.map)
        plt.plot(self.entrada[1]+0.5, self.entrada[0]+0.5,'rs')
        plt.show()
        
        print(self.map)

    def vis_caminho(self,caminho):

        plt.axes().invert_yaxis()
        plt.pcolormesh(self.map)

        for i in range(len(caminho)-1):
            plt.plot([caminho[i][1]+0.5,caminho[i+1][1]+0.5],[caminho[i][0]+0.5,caminho[i+1][0]+0.5],'-rs')
        plt.show()


    def get_vizinhos(self,posicao):

        n_lin, n_cols = self.map.shape
        vizinhos = []

        v = []
        v.append(posicao + np.array([1,0])) # norte
        v.append(posicao - np.array([1,0])) # sul
        v.append(posicao + np.array([0,1])) # leste
        v.append(posicao - np.array([0,1])) # oeste
        
        for vi in v:
            if (vi[0] >= 0) and (vi[0] < n_lin) and (vi[1] >= 0) and (vi[1] < n_cols):
                if self.map[vi[0]][vi[1]] <= 0.3 :
                    vizinhos.append(vi) 
        
        return vizinhos

    def percepcoes_iniciais(self):
        return {'posicao':self.entrada,
                'saida':self.saida,
                'vizinhos': self.get_vizinhos(self.entrada)}
    
    def muda_estado(self,acao):

        posicao = acao['mover_para']

        return {'posicao': posicao,
                'saida':self.saida,
                'vizinhos': self.get_vizinhos(posicao)}

if __name__ == '__main__':

    nlin = 10
    ncol = 10

    l1 = Labirinto(nlin,ncol,0.25,[0,0],[nlin-1,ncol-1]) 

    l1.vis_caminho(np.array([[0,0],[0,1],[0,2],[1,2],[2,2]]))

    print(l1.get_vizinhos([3,3]))