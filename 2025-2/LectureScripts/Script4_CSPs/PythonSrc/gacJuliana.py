from copy import deepcopy
from collections import deque


def print_to_do(to_do):
    
    s = '['
    for edge in to_do:
        s += f'<{edge['X']}, {edge['c']['str']}>, '
    s += ']'

    print(s) 



def GAC(G, D):
    
    to_do = deque(deepcopy(G))

    while to_do:
        print_to_do(to_do)
        
        a = to_do.popleft() 
        X = a['X']
        c = a['c']

        
        Y = (c['Scope'] - {X}).pop()

        ND = set()

        
        for x_val in D[X]:
            found_support = False
            for y_val in D[Y]:
                
                if c['Cs'](x_val, y_val):
                    found_support = True
                    break 
            
            if found_support:
                ND.add(x_val)

        
        if ND != D[X]:
            D[X] = ND
            
            
            if not D[X]:
                return D 

           
            for edge in G:
                if X in edge['c']['Scope'] and edge['X'] != X:
                    to_do.append(edge)

    return D

if __name__ == '__main__':
    
    # Definição das Restrições
    # Removi o lambida e difini  funções explícitas que recebem (Val_X, Val_Y)
    
   
    def check_A_less_B(a_val, b_val): return a_val < b_val
    def check_B_greater_A(b_val, a_val): return a_val < b_val 
    def check_B_less_C(b_val, c_val): return b_val < c_val
    def check_C_greater_B(c_val, b_val): return b_val < c_val

    G = [
        {'X':'A', 'c':{'Cs': check_A_less_B,  'Scope':{'A','B'}, 'str': 'A < B'}},
        {'X':'B', 'c':{'Cs': check_B_greater_A, 'Scope':{'A','B'}, 'str': 'A < B'}},
        {'X':'B', 'c':{'Cs': check_B_less_C,  'Scope':{'B','C'}, 'str': 'B < C'}},
        {'X':'C', 'c':{'Cs': check_C_greater_B, 'Scope':{'B','C'},'str': 'B < C'}}
    ]

    D = {
        'A': {1, 2, 3, 4},
        'B': {1, 2, 3, 4},
        'C': {1, 2, 3, 4}
    }

    result = GAC(G, D)
    print("Resultado Final:", result)
   