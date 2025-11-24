from gac_24_11_2025 import GAC

def is_complete(s):

    for e in s:
        if e == -1:
            return False

    return True

def is_consistent(s,pos,v):
    return s[pos-1] < v

def backtracking_all(s,D):

    if is_complete(s):
        print(s)
        return
    
    pos = None

    #len(s) == 3
    #range(len(s)) = range(3) = [0,1,2]

    for i in range(len(s)):
        if s[i]==-1:
            pos = i
            break

    for v in D[pos]:
        if is_consistent(s,pos,v):
            s[pos] = v
            backtracking_all(s,D)
            s[pos] = -1

    return

def backtracking(s,D):

    if is_complete(s):
        return s
    
    pos = None

    #len(s) == 3
    #range(len(s)) = range(3) = [0,1,2]

    for i in range(len(s)):
        if s[i]==-1:
            pos = i
            break

    for v in D[pos]:
        if is_consistent(s,pos,v):
            s[pos] = v
            result = backtracking(s,D)
            if result != -1:
                return result
            s[pos] = -1

    return -1

if __name__ == '__main__':

    G = [{'X':'A','c':{'Cs':lambda A,B: A<B,'Scope':{'A','B'},'str': 'A < B'}},
        {'X':'B','c':{'Cs':lambda B,A: A<B,'Scope':{'A','B'},'str': 'A < B'}},
        {'X':'B','c':{'Cs':lambda B,C: B<C,'Scope':{'B','C'},'str': 'B < C'}},
        {'X':'C','c':{'Cs':lambda C,B: B<C,'Scope':{'B','C'},'str': 'B < C'}}]

    D = {'A':{1,2,3,4},
        'B':{1,2,3,4},
        'C':{1,2,3,4}}
    
    D = GAC(G,D)

    print(D)

    ND = []
    for key in D:
        ND.append(D[key])

    print(ND)

    print(backtracking([-1,-1,-1],ND))

    backtracking_all([-1,-1,-1],ND)

        
