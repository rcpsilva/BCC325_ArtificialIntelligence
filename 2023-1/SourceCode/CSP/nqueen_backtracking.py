import pygame
import sys

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


def same_column(sol,col):
    return (col in sol)

def same_diagonal(sol,col):

    for i in range(len(sol)):
        delta_col = abs(col-sol[i]) 
        delta_row = abs(i-len(sol))

        if delta_col==delta_row:
            return True
        
    return False

def violate_constraints(sol,col,constraints):
    for c in constraints:
        res = c(sol,col)
        if res:
           return True

    return False 

def backtracking(n,constraints,sol=[]):

    if len(sol)==n:
        return sol
    
    for col in [int(i) for i in range(n)]:
        if not violate_constraints(sol,col,constraints):
            sol.append(col)
            res = backtracking(n,constraints,sol)
            if res:
                return res
            sol.pop(-1)
            

if __name__ == '__main__':

    constraints = [same_diagonal,same_column]
    n = 60

    res = backtracking(n,constraints)
    print(res)

    draw_chessboard(res)