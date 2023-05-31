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

def r0e7(sol,val):
    if len(sol) > 0:
        return sol[0] == 7

    return True

def different_column(sol,val):
    return not (val in sol)

def different_diagonal(sol,val):
    
    for i in range(len(sol)):
        deltay = abs(sol[i]-val)
        deltax = abs(i - len(sol))
        if (deltay == deltax):
            return False

    return True

def check_constraints(sol,val,constraints):

    for c in constraints:
        if not c(sol,val):
            return False

    return True


def search(domain, constraints, sol=[]):

    if len(sol) == len(domain):
        return sol
    else:
        for d in domain[len(sol)]:
            if check_constraints(sol, d, constraints):
                sol.append(d)
                result = search(domain,constraints,sol)
                if result:
                    return result
                sol.pop(-1)

# def draw_chessboard(queen_positions):
#     n = len(queen_positions)
#     board = [['-'] * n for _ in range(n)]

#     for row, col in enumerate(queen_positions):
#         board[row][col] = 'Q'

#     for row in range(n):
#         for col in range(n):
#             print(board[row][col], end=' ')
#         print()

if __name__ == '__main__':
    
    n = 4
    domain = [[i for i in range(n)] for j in range(n)]
    constraints = [different_column, different_diagonal]
    
    print(domain)
    result = search(domain, constraints)
    print(result)
    draw_chessboard(result)