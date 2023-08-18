def bu(kb):
    c = []
    added_atom = True

    for a in kb['askables']:
        if ask(a):
            c.append(a)

    while added_atom:
        added_atom = False
        for head in kb['rules']:
            bodies = kb['rules'][head]
            for body in bodies:
                if not set(body).difference(set(c)):
                    if not head in c:
                        added_atom = True
                        c.append(head)
    return c

def td(querry,kb):

    print(querry)

    if not querry:
        return 'yes.'
    else:
        a = querry.pop(0)

        if a in kb['askables']:
            if not ask(a):
                print(f'Não é possível provar {a}. ')
                return None
            else:
                ans = td(querry,kb)
                if ans == 'yes.':
                    return 'yes.'

        
        if a in kb['rules']:
            bodies = kb['rules'][a]
            for b in bodies:
                ans = td(b + querry,kb)
                if ans == 'yes.':
                    return 'yes.'


        print(f'Não é possível provar {a}. ')
        return None
    
def explain(observacoes,kb,explicacao=set()):

    if not observacoes:
        return [explicacao]
    else:
        o = observacoes.pop(0)

        if o in kb['assumables']:
            return explain(observacoes,kb,explicacao|{o})
        elif o in kb['rules']:
            bodies = kb['rules'][o]
            explicacoes = []
            for b in bodies:
                explicacoes += explain(b + observacoes, kb, explicacao)

            return explicacoes
        
        return [explicacao]
            


def get_minimal_explanations(explicacoes):

    not_minimal = []

    for i in range(len(explicacoes)):
        for j in range(len(explicacoes)):
            if i != j:
                if explicacoes[j].issubset(explicacoes[i]):
                    not_minimal.append(i)

    return [explicacoes[i] for i in range(len(explicacoes)) if i not in not_minimal]


def ask(askable):
    ans = input(f'({askable}) é verdadeiro? ')
    return True if ans.lower() in ['sim','s','yes','y'] else False

if __name__ == '__main__':

    kb = {'rules': {'a':[['b','c']],
                    'b':[['d'],['e']],
                    'c':[[]],
                    'd':[['h']],
                    'g':[['a','b','c']],
                    'f':[['h','b']]},
        'askables':['e'],
        'assumable':[]}

    #print(bu(kb))

    #print(td(['g'],kb))

    kb = {'rules': {'bronquite':[['gripe'],['fumante']],
                    'tosse':[['bronquite']],
                    'dispineia':[['bronquite']],
                    'febre':[['gripe'],['infecção']],
                    'dor_gargante':[['gripe']],
                    'falso':[['fumante','não_fumante']]},
        'askables':[],
        'assumables':['fumante','infecção','gripe']}
    
    explanations = explain(['dispineia','febre'],kb)
    print(explanations)

    print(get_minimal_explanations(explanations))