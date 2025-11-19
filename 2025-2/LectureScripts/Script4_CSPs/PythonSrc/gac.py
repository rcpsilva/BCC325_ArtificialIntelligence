from copy import deepcopy

def GAC(G,D):
    
    to_do = deepcopy(G)

    while to_do:
        a = to_do.pop(0)
        X = a['X']
        c = a['c']

        Y = c['Scope'] - {X}
        Y = Y.pop()

        ND = []

        for v in D[X]:
            for y in D[Y]:
                if c['Cs'](v,y):
                    ND.append(v)
                    break

        if set(ND) != D[X]:
            D[X] = set(ND)

            for edge in G:
                if X in edge['c']['Scope'] and c['id'] != edge['c']['id']:
                    Z = edge['c']['Scope'] - {X}
                    to_do.append({'X':Z.pop(),'c':edge['c']})

    return D

if __name__ == '__main__':

    # X = {A,B,C}
    # D = {{1,2,3,4},{1,2,3,4},{1,2,3,4}}
    # C = {A<B,B<C}

    G = [{'X':'A','c':{'Cs':lambda A,B: A<B,'Scope':{'A','B'},'id':0}},
        {'X':'B','c':{'Cs':lambda B,A: A<B,'Scope':{'A','B'},'id':0}},
        {'X':'B','c':{'Cs':lambda B,C: B<C,'Scope':{'B','C'},'id':1}},
        {'X':'C','c':{'Cs':lambda C,B: B<C,'Scope':{'B','C'},'id':1}}]

    D = {'A':{1,2,3,4},
        'B':{1,2,3,4},
        'C':{1,2,3,4}}

    #print(G.pop(0))

    print(GAC(G,D))
    


