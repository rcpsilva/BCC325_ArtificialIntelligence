# Local Search 
#
# Entradas: Variáveis (X), Domínio (D), Restrições (C)
# Saída: Atribuição total que satisfaz as restrições
#
# Para cada variável xi em X:
#   Seleciona aleatoriamente um valor de D[xi]
# 
# Equanto as restrições não são atendidas
#   Selecionar aleatoriamente uma variável xi em X
#   Selecionar aleatoriamente um valor de D[xi] e atribuir à xi


# Primeira melhora (First improvement)
#
# Entradas: Variáveis (X), Domínio (D), Restrições (C)
# Saída: Atribuição total que satisfaz as restrições
#
# sol = []
# Para cada variável xi em X:
#   Seleciona aleatoriamente um valor de D[xi]
#   sol = sol U xi
# 
# Enquanto !criterio_de_parada: 
#   sol'= vizinho(sol)
#   se f(sol') <= f(sol):
#       sol = sol'

# Critérios de parada
#   1 - Conflitos
#   2 - Mínimo local
#   3 - Tempo máximo (número de iteraçoes)

import pygame
import sys
import numpy as np
from copy import copy

def draw_chessboard(queen_positions):

    queen_positions = [(i,queen_positions[i]) for i in range(len(queen_positions))]

    # Set up colors
    BLACK = (107,142,35)
    WHITE = (255,248,220)
    RED = 	(0,0,0)

    # Set up the window size
    WIDTH = 480
    HEIGHT = 480

    # Calculate cell width and height
    CELL_SIZE = WIDTH // len(queen_positions)

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chessboard')

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the chessboard
        for row in range(len(queen_positions)):
            for col in range(len(queen_positions)):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if (row, col) in queen_positions:
                    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

        # Update the display
        pygame.display.flip()


def get_conflicts(sol):
    conflicts = 0

    for i in range(len(sol)):
        for j in range(i+1,len(sol)):
            delta_col = abs(sol[i]-sol[j]) 
            delta_row = abs(i-j)

            if delta_col==delta_row:
                conflicts+=1

    return conflicts

def local_search(n,f,itermax=1000,sol=[]):

    conflicts = []

    # Construir solução inicial
    if not sol:
        for i in range(n):
            r = np.random.randint(n)
            while r in sol:
                r = np.random.randint(n)
            sol.append(r) 

    iter = 0
    while iter < itermax:
        print(f(sol))
        # Gerar vizinho
        i = np.random.randint(n)
        j = np.random.randint(n)

        vizinho = copy(sol)
        vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
        if f(vizinho) <= f(sol):
            sol = vizinho 
            conflicts.append(f(vizinho))

        iter += 1

    print(f(sol))
    return sol,conflicts

if __name__ == '__main__':

    n = 10

    res, conflicts = local_search(n,get_conflicts)
    #print(res)

    draw_chessboard(res)

   