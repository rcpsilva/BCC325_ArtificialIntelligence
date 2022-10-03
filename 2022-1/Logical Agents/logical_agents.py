def botton_up(kb):
    C = []

    if 'askables' in kb:
        for a in kb['askables']:
            if ask(a):
                C.append(a)

    new_consequence = True

    while new_consequence:
        new_consequence = False 

        for head in kb['rules']:
            if head not in C: # Very inneficent
                for body in kb['rules'][head]:
                    if not set(body).difference(set(C)): # Very innefient
                        C.append(head)
                        new_consequence = True

    return C

def top_down(querry,kb):

    print(querry)

    if not querry:
        return 'yes.'
    else:
        a = querry.pop(0)
        
        if a in kb['askables']:
            a_val = ask(a)
            kb['askables'].remove(a)
            if a_val:
                kb['rules'][a] = [[]]

        if a not in kb['rules']:
            return f'Cannot prove {querry}'
        
        bodies = kb['rules'][a]
        
        for b in bodies:
            res = top_down(b + querry,kb)
            if res == 'yes.':
                return res
        
        return f'Cannot prove {querry}.'


def ask(askable):
    ans = input(f'Is {askable} true?')
    return True if ans.lower() in ['sim','s','yes','y'] else False

def explain(observations,kb,explanation=set()):

    if observations:
        o = observations[0]

        if o in kb['assumables']:
            return explain(observations[1:],kb,explanation|{o})
        else:
            bodies = kb['rules'][o]
            explanations = []

            for body in bodies:
                explanations += explain(body + observations[1:],kb,explanation)

            return explanations

    return [explanation]


def get_minimal_explanations(explanations):

    not_minimal = []

    for i in range(len(explanations)):
        for j in range(len(explanations)):
            if explanations[i].issubset(explanations[j]) and i != j:
                not_minimal.append(j)

    return [explanations[i] for i in range(len(explanations)) if i not in not_minimal]



if __name__ == "__main__":
    
    kb = {'rules':{'a':[['b','c']],
                   'b':[['d'],['c']],
                   'd':[['h']],
                   'g':[['a','b','c']],
                   'f':[['h','b']]},
            'askables':['c','e']}


    #print(top_down(['g'],kb))

    #print(botton_up(kb))

    kb2 = {  'rules':{  'bronchitis':[['influenza'],['smokes']],
                        'coughing':[['bronchitis']],
                        'wheezing':[['bronchitis']],
                        'fever':[['influenza'],['infection']],
                        'sore_throat':[['influenza']],
                        'False':[['smokes','non-smoker']]
                        },
            'assumables':['smokes','influenza','infection'] }+

    explanations = explain(['wheezing','fever'],kb2)

    print(explanations)

    print(get_minimal_explanations(explanations))