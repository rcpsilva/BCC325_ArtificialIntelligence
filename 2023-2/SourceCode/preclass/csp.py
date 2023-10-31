import os
import time
from copy import copy, deepcopy
import json

def print_graph(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
        print_graph(value, indent+1)
      else:
        v = value[0]
        if isinstance(v,Constrait):
            for c in value:
                print('\t' * (indent+1) + f'{c.scope}:{c.bool_func}')
        else:
            print('\t' * (indent+1) + f'{value}')

class Constrait():
    def __init__(self,scope=None,bool_func=None):
        self.scope = scope
        self.bool_func = bool_func
    
    def eval(self,vals):
        return self.bool_func(vals)

def create_sudoku_constraint(pos1, pos2):

    c = Constrait()
    c.scope = [pos1,pos2]
    c.bool_func = lambda x, y: x!=y

    return c

def generate_constraint_graph(sudoku):

    domains = {}
    graph = {}

    for i in range(len(sudoku)):
        for j in range(len(sudoku)):

            domains[(i,j)] = [sudoku[i][j]] if sudoku[i][j]!=0 else [i for i in range(1,10)]

            if sudoku[i][j]==0:


                # Row constraints
                graph[(i,j)] = []
                

                for k in range(len(sudoku)):
                    if k != j:
                        graph[(i,j)].append(create_sudoku_constraint((i,j), (i,k)))

                # Column constraints
                for k in range(len(sudoku)):
                    if k != i:
                        graph[(i,j)].append(create_sudoku_constraint((i,j), (k,j)))

                # group constraints
                iquad = (i//3)*3
                jquad = (j//3)*3

                for k in range(iquad,iquad+3):
                    for l in range(jquad,jquad+3):
                        if (i,j)!=(k,l):
                            graph[(i,j)].append(create_sudoku_constraint((i,j), (k,l)))
    return graph,domains

def GAC(graph,domains):

    to_do = []

    for key in graph:
        for c in graph[key]:
            to_do.append((key,c))

    while to_do:
        edge = to_do.pop(0)
        X = edge[0]
        const = edge[1]
        Y = const.scope[1]
        domx = domains[edge[0]]
        domy = domains[Y]

        new_dom = []

        for x in domx:
            for y in domy:
                if const.bool_func(x,y):
                    new_dom.append(x)
                    break 
        
        if len(domx)!= len(new_dom):
            domains[X] = new_dom

            for key in graph:
                if key!=X:
                    for c in graph[key]:
                        if c.scope[1] == X:
                            to_do.append((key,c))

    return domains
    
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

    graph,domains = generate_constraint_graph(evil_game)

    #print_graph(graph)
    #print_graph(domains)

    domains = GAC(graph,domains)

    print_graph(domains)
