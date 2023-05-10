import numpy as np

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
        print(self.map)

    def get_vizinhos(self,posicao):

        n_lin, n_cols = self.map.shape
        vizinhos = []

        v = []
        v.append(posicao + np.array([1,0])) # norte
        v.append(posicao - np.array([1,0])) # sul
        v.append(posicao + np.array([0,1])) # leste
        v.append(posicao - np.array([0,1])) # oeste
        
        for vi in v:
            if (0 <= vi[0] < n_lin) and (0 <= vi[1] < n_cols):
                if self.map[vi[0]][vi[1]] == 0:
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

    l1 = Labirinto(5,6,0.5,[0,0],[4,5]) 

    l1.vis_map()

    print(l1.get_vizinhos([3,3]))