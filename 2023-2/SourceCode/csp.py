import os
import time

def print_game(game):
    os.system('cls')
    print()
    for row in game:
        print(row)
    time.sleep(0.3)

def backtrack(sol,
              is_solution,
              get_var,
              domain_func,
              is_valid,
              attach_func,
              detach_func,
              print_sol=print):
    if is_solution(sol):
        print_sol(sol)
    else:
        pos = get_var(sol)
        for v in domain_func(sol,pos):
            if is_valid(v,pos,sol):
                attach_func(v,pos,sol)
                backtrack(sol,
                    is_solution,
                    get_var,
                    domain_func,
                    is_valid,
                    attach_func,
                    detach_func,
                    print_sol)
                detach_func(v,pos,sol)

class abc_problem:
    def __init__(self,n):
        self.n = n

    def is_solution(self,sol):
        return len(sol) == self.n
    
    def get_var(self,sol):
        return len(sol)
    
    def domain_func(self,sol,pos):
        return [i for i in range(1,self.n+2)]
    
    def is_valid(self,v,pos,sol):
        if pos == 0:
            return True
        else:
            return v > sol[pos-1]
    
    def attach_func(self,v,pos,sol):
        sol.append(v)

    def detach_func(self,v,pos,sol):
        sol.pop(-1)

class sudoku:
    def __init__(self):
        pass

    def is_solution(self,sol):
        for i in range(9):
            for j in range(9):
                if sol[i][j] == 0:
                    return False
        
        return True
    
    def get_var(self,sol):
        for i in range(9):
            for j in range(9):
                if sol[i][j] == 0:
                    return [i,j]
                
    def domain_func(self,sol,pos):
        return [i for i in range(1,10)]
    
    def is_valid(self,v,pos,sol):

        if v in sol[pos[0]]:
            return False
        
        for i in range(9):
            if v == sol[i][pos[1]]:
                return False
            
        iquad = (pos[0]//3)*3
        jquad = (pos[1]//3)*3

        for i in range(iquad,iquad+3):
            for j in range(jquad,jquad+3):
                if v == sol[i][j]:
                    return False
                
        return True
    
    def attach_func(self,v,pos,sol):
        sol[pos[0]][pos[1]] = v
    
    def detach_func(self,v,pos,sol):
        sol[pos[0]][pos[1]] = 0

    def print_func(self,sol):
        os.system('cls')
        print()
        for row in sol:
            print(row)


    
if __name__ == '__main__':

    abc = abc_problem(6)
    sol = []
    backtrack(sol,
              abc.is_solution,
              abc.get_var,
              abc.domain_func,
              abc.is_valid,
              abc.attach_func,
              abc.detach_func)
    
    easy_game = [[0,0,0,7,5,0,4,9,0],
             [0,4,5,6,9,0,0,1,8],
             [0,0,6,0,0,0,7,0,0],
             [9,8,0,2,0,0,0,0,0],
             [2,0,7,1,0,8,0,0,0],
             [0,0,3,0,0,5,8,0,7],
             [4,2,0,0,6,7,1,8,0],
             [5,0,0,0,2,0,0,7,4],
             [3,0,0,5,1,0,9,0,2]]


    sdk = sudoku()

    backtrack(easy_game,
              sdk.is_solution,
              sdk.get_var,
              sdk.domain_func,
              sdk.is_valid,
              sdk.attach_func,
              sdk.detach_func,
              sdk.print_func)


