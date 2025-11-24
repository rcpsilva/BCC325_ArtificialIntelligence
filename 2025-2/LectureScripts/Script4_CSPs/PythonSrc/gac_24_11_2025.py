from copy import deepcopy

def print_to_do(to_do):
    
    s = '['
    for edge in to_do:
        s += f'<{edge['X']}, {edge['c']['str']}>, '
    s += ']'

    print(s) 


def GAC(G,D):
    
    to_do = deepcopy(G)

    while to_do:
        print_to_do(to_do)

        a = to_do.pop(0)
        X = a['X']
        c = a['c']

        Y = c['Scope'] - {X}
        Y = Y.pop()

        ND = set()

        for v in D[X]:
            for y in D[Y]:
                if c['Cs'](v,y):
                    ND.add(v)
                    break

        if ND != D[X]:
            D[X] = ND

            for edge in G:
                if X in edge['c']['Scope']:
                    if c['str'] != edge['c']['str']:
                        if edge['X'] != X:
                            to_do.append(edge)

    return D

if __name__ == '__main__':

    # X = {A,B,C}
    # D = {{1,2,3,4},{1,2,3,4},{1,2,3,4}}
    # C = {A<B,B<C}

    G = [{'X':'A','c':{'Cs':lambda A,B: A<B,'Scope':{'A','B'},'str': 'A < B'}},
        {'X':'B','c':{'Cs':lambda B,A: A<B,'Scope':{'A','B'},'str': 'A < B'}},
        {'X':'B','c':{'Cs':lambda B,C: B<C,'Scope':{'B','C'},'str': 'B < C'}},
        {'X':'C','c':{'Cs':lambda C,B: B<C,'Scope':{'B','C'},'str': 'B < C'}}]

    D = {'A':{1,2,3,4},
        'B':{1,2,3,4},
        'C':{1,2,3,4}}

    #print(G.pop(0))

    print(GAC(G,D))
    


