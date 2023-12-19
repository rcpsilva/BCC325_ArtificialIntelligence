class Agent:
    def __init__(self, ambiente) -> None:
        self.ambiente = ambiente
        self.percepcoes = ambiente.percepcoes_iniciais()
        self.F = [[self.percepcoes['posicao']]]
        self.C = []
        self.H = []
        self.C_H = []

    def act(self):
        
        while self.F:
            path = self.F.pop(0)
            
            action = {'mover_para':path[-1]}

            self.percepcoes = self.ambiente.muda_estado(action) 

            if (self.percepcoes['posicao'] == self.percepcoes['saida']).all():
                return path
            else:
                for vi in self.percepcoes['vizinhos']:
                    self.F.append(path + [vi])
        