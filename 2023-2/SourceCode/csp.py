import os
import time

def print_graph(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
        print_graph(value, indent+1)
      else:
        v = value[0]
        if isinstance(v,Constraint):
            for c in value:
                print('\t' * (indent+1) + f'{c.scope}:{c.bool_func}')
        else:
            print('\t' * (indent+1) + f'{value}')

class Constraint():
    def __init__(self,scope,bool_func):
        self.scope = scope
        self.bool_func = bool_func

def generate_graph_sudoku(sudoku):

    domains = {}
    graph = {}

    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            
            domains[(i,j)] = [sudoku[i][j]]  if sudoku[i][j]!=0 else [k for k in range(1,10)]

            if sudoku[i][j] == 0:
                graph[(i,j)] = []
                #row constraints
                for k in range(len(sudoku)):
                    if k != j:
                        graph[(i,j)].append(Constraint([(i,j),(i,k)],lambda v1,v2 : v1!=v2))

                # column constrainst
                for k in range(len(sudoku)):
                    if k != i:
                        graph[(i,j)].append(Constraint([(i,j),(k,j)],lambda v1,v2 : v1!=v2))

                # Quadrant constraints
                iquad = (i//3)*3
                jquad = (j//3)*3

                for k in range(iquad,iquad+3):
                    for l in range(jquad,jquad+3):
                        if (i,j)!=(k,l):
                            graph[(i,j)].append(Constraint([(i,j),(k,l)],lambda v1,v2 : v1!=v2))

    return graph,domains

def GAC(graph,domains):
    to_do = []

    for var in graph:
        for c in graph[var]:
            to_do.append((var,c))

    while to_do:
        edge = to_do.pop(0)
        X = edge[0]
        c = edge[1]
        Y = c.scope[1]

        domX = domains[X]
        domY = domains[Y]

        ND = []

        for x in domX:
            for y in domY:
                if c.bool_func(x,y):
                    ND.append(x)
                    break
        
        if len(ND)!=len(domX):
            domains[X] = ND

            for var in graph:
                if var != X:
                    for c in graph[var]:
                        if c.scope[1] == X:
                            to_do.append((var,c))

    return domains

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

    easy_game = [[0,0,0,7,5,0,4,9,0],
             [0,4,5,6,9,0,0,1,8],
             [0,0,6,0,0,0,7,0,0],
             [9,8,0,2,0,0,0,0,0],
             [2,0,7,1,0,8,0,0,0],
             [0,0,3,0,0,5,8,0,7],
             [4,2,0,0,6,7,1,8,0],
             [5,0,0,0,2,0,0,7,4],
             [3,0,0,5,1,0,9,0,2]]
    
    medium = [[0,0,0,0,5,1,0,0,0],
             [5,6,1,9,0,0,0,0,0],
             [4,0,0,7,0,0,0,0,0],
             [0,0,2,0,0,5,4,0,0],
             [0,4,5,0,0,0,0,0,8],
             [1,9,0,0,4,0,0,0,3],
             [0,8,0,0,2,7,0,3,1],
             [6,0,0,0,0,0,0,2,0],
             [0,5,0,8,0,0,6,4,9]]

    evil_game = [[1,0,0,0,0,9,0,0,0],
             [0,0,0,0,2,0,4,0,0],
             [0,5,9,8,0,0,0,0,3],
             [6,0,0,7,0,0,0,0,0],
             [0,1,7,0,0,4,3,0,0],
             [8,0,0,0,0,0,0,0,1],
             [0,0,0,0,0,8,0,9,0],
             [0,7,3,9,0,0,0,0,5],
             [0,0,6,0,0,0,0,0,0]]

    graph,domains = generate_graph_sudoku(evil_game)

    #print_graph(graph)
    print_graph(domains)

    domains = GAC(graph,domains)
    print('------------GAC-------------------')
    print_graph(domains)


    #sdk = sudoku()

    #backtrack(easy_game,
    #          sdk.is_solution,
    #          sdk.get_var,
    #          sdk.domain_func,
    #          sdk.is_valid,
    #          sdk.attach_func,
    #          sdk.detach_func,
    #          sdk.print_func)


