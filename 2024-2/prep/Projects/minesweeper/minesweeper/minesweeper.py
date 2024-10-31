import itertools
import random
from copy import deepcopy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        return self.cells if self.count == len(self.cells) else set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        return self.cells if self.count == 0 else set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells = self.cells - {cell}
            self.count = self.count - 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells = self.cells - {cell}


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1)
        self.moves_made.add(cell)

        # 2) 
        self.mark_safe(cell)

        # 3)
        cells = set()
        for i in range(cell[0]-1,cell[0]+2):
            for j in range(cell[1]-1,cell[1]+2):
                if 0<=i<self.height and 0<=j<self.width:
                    if ((i,j) not in self.safes) and ((i,j) not in self.mines):
                        cells.add((i,j))
                    elif ((i,j) in self.mines):
                        count -= 1

        self.knowledge.append(Sentence(cells=cells, count=count))

        new_knowledge_added = True
        while new_knowledge_added:
            
            print(f'move: {cell} count: {count}')
            self.print_knowledge()
            new_knowledge_added = False
            
            # 4)
            self.knowledge = [k for k in self.knowledge if k.cells]

            nsafes = len(self.safes)
            nmines = len(self.mines)
            
            for sentence in self.knowledge:
                self.safes |= sentence.known_safes()
                self.mines |= sentence.known_mines()

            if nsafes < len(self.safes) or nmines < len(self.mines):
                new_knowledge_added = True    

            for cell in self.mines:
                for sentence in self.knowledge:
                    sentence.mark_mine(cell)

            for cell in self.safes:
                for sentence in self.knowledge:
                    sentence.mark_safe(cell)

            # 5) 
            new_knowledge = deepcopy(self.knowledge)
            for s1 in self.knowledge:
                for s2 in self.knowledge:
                    if s1 != s2:
                       if s1.cells and s2.cells:
                           if s1.cells.issubset(s2.cells):
                                if s2.cells-s1.cells:
                                    if Sentence(cells=s2.cells-s1.cells, count=s2.count-s1.count) not in self.knowledge:
                                        new_knowledge.append(Sentence(cells=s2.cells-s1.cells, count=s2.count-s1.count))
                                        new_knowledge_added = True

            self.knowledge = deepcopy(new_knowledge)


    def print_knowledge(self):
        print('----------------KB------------------')
        for k in self.knowledge:
            print(k)
        print(f'-----------------------------')
        print(f'safes: {self.safes}')
        print(f'mines: {self.mines}')
        print(f'moves: {self.moves_made}')
        print('-----------------------------------')


    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        for move in self.safes:
            if move not in self.moves_made:
                return move
            
        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        rows = list(range(self.height))
        cols = list(range(self.width))

        random.shuffle(rows)
        random.shuffle(cols)

        for i in rows:
            for j in cols:
                if ((i,j) not in self.moves_made) and ((i,j) not in self.mines):
                    return (i,j) 

        return None
    
if __name__ == '__main__':
    ai = MinesweeperAI(height=4, width=5)
    ai.add_knowledge((2, 4), 1)
    ai.add_knowledge((2, 3), 1)
    ai.add_knowledge((1, 4), 0)
    ai.add_knowledge((3, 2), 0)
    expected = {(3, 4)}
    result = ai.mines

    print(ai.mines)

