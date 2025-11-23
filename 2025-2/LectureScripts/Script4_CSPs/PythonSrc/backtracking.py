from gac2 import GAC

def is_valid(sol,v):

    if len(sol) == 0:
        return True

    if v > sol[-1]:
        return True
    
    return False

def is_complete(sol):

    if len(sol)==3:
        return True
    
    return False


def backtracking(Xs, D, sol=[]):
    print(sol)
    if is_complete(sol):
        print(f' - {sol}')
        return
    
    next = len(sol)

    for v in D[Xs[next]]:
        if is_valid(sol,v):
            sol.append(v)
            backtracking(Xs,D,sol)
            sol.pop(-1) 

def backtracking2(Xs, D, sol=[]):
    
    print(sol)
    if is_complete(sol):
        return sol
    
    next = len(sol)

    for v in D[Xs[next]]:
        if is_valid(sol,v):
            sol.append(v)
            result = backtracking2(Xs,D,sol)
            if result == -1:
                sol.pop(-1)
            else:
                return result

    return -1    

if __name__ == '__main__':

    G = [{'X':'A','c':{'Cs':lambda A,B: A<B,'Scope':{'A','B'},'str': 'A < B'}},
        {'X':'B','c':{'Cs':lambda B,A: A<B,'Scope':{'A','B'},'str': 'A < B'}},
        {'X':'B','c':{'Cs':lambda B,C: B<C,'Scope':{'B','C'},'str': 'B < C'}},
        {'X':'C','c':{'Cs':lambda C,B: B<C,'Scope':{'B','C'},'str': 'B < C'}}]

    D = {'A':{1,2,3,4},
        'B':{1,2,3,4},
        'C':{1,2,3,4}}
    
    Xs = [k for k in D]

    print('FIRST =========================')

    backtracking2(Xs,D)

    print('FULL =========================')

    backtracking(Xs,D)

    print(D)
    ND = GAC(G,D)
    print(ND)

    print('FULL + GAC =========================')

    backtracking(Xs,ND)
   






