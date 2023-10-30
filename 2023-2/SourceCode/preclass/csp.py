import os
import time

class constrait():
    def __init__(self,scope,bool_func):
        self.scope = scope
        self.bool_func = bool_func
    
    def eval(self,vals):
        return self.bool_func(vals)
    
def backtrack_return(sol,solution_func,get_var_position,domain_func,atach_func,detach_func,is_valid):
    if solution_func(sol):
        return sol
    else:
        pos = get_var_position(sol)
        for v in domain_func(sol,pos):
            if is_valid(v,pos,sol):
                atach_func(v,pos,sol)
                solution = backtrack_return(sol,solution_func,get_var_position,domain_func,atach_func,detach_func,is_valid)
                if solution:
                    return solution
                detach_func(v,pos,sol)

def backtrack(sol,
              solution_func,
              get_var_position,
              domain_func,
              atach_func,
              detach_func,
              is_valid, 
              print_func):
    
    if solution_func(sol):
        print_func(sol)
        return 
    else:
        pos = get_var_position(sol)
        for v in domain_func(sol,pos):
            if is_valid(v,pos,sol):
                atach_func(v,pos,sol)
                backtrack(sol,solution_func,get_var_position,domain_func,atach_func,detach_func,is_valid,print_func)
                detach_func(v,pos,sol)

class abc_problem:
    def __init__(self,sol):
        self.sol = sol

    def solution_func(self, sol):
        return len(sol) == 3
    
    def get_var_position(self,sol):
        return len(sol)
    
    def domain_func(self,sol,pos):
        return [1,2,3,4]
    
    def atach_func(self,v,pos,sol):
        sol.append(v)
    
    def detach_func(self,v,pos,sol):
        sol.pop(-1)
    
    def is_valid(self,v,pos,sol):
        if pos == 0:
            return True
        else:
            return sol[pos-1] < v

class sudoku_problem:
    def __init__(self, game):
        self.game = game

    def print_game(self,game):
        print()
        for row in game:
            print(row)

    def is_solution_sudoku(self,sol):
        for i in range(9):
            for j in range(9):
                if sol[i][j] == 0:
                    return False

        return True

    def atach_sudoku(self,v,pos,sol):
        sol[pos[0]][pos[1]] = v

    def detach_sudoku(self,v,pos,sol):
        sol[pos[0]][pos[1]] = 0

    def get_var_position_sudoku(self,sol):
        for i in range(9):
            found = False
            for j in range(9):
                if sol[i][j]==0:
                    found = True
                    break
            if found:
                break

        return [i,j]

    def domain_sudoku(self,sol,pos):
        return [i for i in range(1,10)]

    def is_valid_sudoku(self,v,pos,sol):
        i = pos[0]
        j = pos[1]

        for cell in sol[i]:
            if v == cell:
                return False
            
        for row in sol:
            if row[j] == v:
                return False
            
        igroup = (i//3)*3
        jgroup = (j//3)*3

        for i in range(3):
            for j in range(3):
                if sol[igroup+i][jgroup+j] == v:
                    return False
        
        return True

if __name__ == '__main__':
    from copy import copy

    easy_game = [[0,0,0,7,5,0,4,9,0],
             [0,4,5,6,9,0,0,1,8],
             [0,0,6,0,0,0,7,0,0],
             [9,8,0,2,0,0,0,0,0],
             [2,0,7,1,0,8,0,0,0],
             [0,0,3,0,0,5,8,0,7],
             [4,2,0,0,6,7,1,8,0],
             [5,0,0,0,2,0,0,7,4],
             [3,0,0,5,1,0,9,0,2]]

    evil_game = [[1,0,0,0,0,9,0,0,0],
             [0,0,0,0,2,0,4,0,0],
             [0,5,9,8,0,0,0,0,3],
             [6,0,0,7,0,0,0,0,0],
             [0,1,7,0,0,4,3,0,0],
             [8,0,0,0,0,0,0,0,1],
             [0,0,0,0,0,8,0,9,0],
             [0,7,3,9,0,0,0,0,5],
             [0,0,6,0,0,0,0,0,0]]

    sdk = sudoku_problem(evil_game)

    backtrack(sdk.game,
              sdk.is_solution_sudoku,
              sdk.get_var_position_sudoku,
              sdk.domain_sudoku,
              sdk.atach_sudoku,
              sdk.detach_sudoku,
              sdk.is_valid_sudoku,
              sdk.print_game)
    
    #print()
    #for row in sdk.game:
    #    print(row)

    sol = []
    abc = abc_problem(sol)

    backtrack(abc.sol,
              abc.solution_func,
              abc.get_var_position,
              abc.domain_func,
              abc.atach_func,
              abc.detach_func,
              abc.is_valid,
              print)
    

   
