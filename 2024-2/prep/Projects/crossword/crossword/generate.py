import sys

from crossword import *
from copy import deepcopy

class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())
        
    def print_domains(self):
        for var in self.domains:
            print(f'{var} : {self.domains[var]}')

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        
        for variable in self.domains:
            new_domain = deepcopy(self.domains[variable])
            for word in self.domains[variable]:
                if len(word) != variable.length:
                    new_domain.remove(word)

            self.domains[variable] = new_domain


    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        def is_good(word_x,word_y,o):
            return word_x[o[0]] == word_y[o[1]]

        overlap = self.crossword.overlaps[(x,y)]
        
        if overlap:
            removals = set()
            for dx in self.domains[x]:
                good_to_go = False
                for dy in self.domains[y]:
                    if is_good(dx,dy,overlap):
                        good_to_go = True

                if not good_to_go:
                    removals.add(dx)
            
            if removals:
                self.domains[x] -= removals
                return True
        
        return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        if arcs == None:
            arcs = [arc for arc in self.crossword.overlaps]
        
        while arcs:
            (x,y) = arcs.pop(0)
            if self.revise(x,y):
                if not self.domains[x]:
                    return False

                additional_arcs = [(z,x) for z in self.crossword.neighbors(x) if z!=y]
                
                arcs += additional_arcs                
                
        return True


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        for var in self.domains:
            if var not in assignment:
                return False
            
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        # check whether the assingments are all different

        for var1 in assignment:
            for var2 in assignment:
                if (var1 != var2) and assignment[var1] and assignment[var2]:
                    if assignment[var1] == assignment[var2]:
                        return False
        
        # check string lengths

        for var in assignment:
            if len(assignment[var]) != var.length:
                return False

        # check overlaps

        for (x,y) in self.crossword.overlaps:
            if self.crossword.overlaps[(x,y)]:
                if (x in assignment) and (y in assignment):
                    olp = self.crossword.overlaps[(x,y)]
                    if assignment[x][olp[0]] != assignment[y][olp[1]]:
                        return False
                
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """

        def n_key(e):
            return e[1]

        l = []

        for val_x in self.domains[var]:
            n = 0
            for y in self.crossword.neighbors(var):
                if y not in assignment:
                    olp = self.crossword.overlaps[(var,y)]
                    if olp:
                        for val_y in self.domains[y]:
                            if val_x[olp[0]] != val_y[olp[1]]:
                                n+=1
            
            l.append((val_x,n))
 
        
        l.sort(key=n_key)
        l = [val for (val,a) in l]

        return l

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """

        def degree(var):
            return len([(x,y) for (x,y) in self.crossword.overlaps if x == var])

        vars = [(len(self.domains[var]),-degree(var),var) for var in self.domains if var not in assignment]
        vars = sorted(vars, key=lambda x: (x[0], x[1]))

        return vars[0][2]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
    
        if self.assignment_complete(assignment):
            return assignment
        
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var,assignment):
            assignment[var] = value
            if self.consistent(assignment):
                result = self.backtrack(assignment)
                if result:
                    return result
            assignment.pop(var)
        
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
