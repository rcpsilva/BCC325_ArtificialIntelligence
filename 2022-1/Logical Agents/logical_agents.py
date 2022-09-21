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
            if head not in C: # Very innefient
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

if __name__ == "__main__":
    
    kb = {'rules':{'a':[['b','c']],
                   'b':[['d'],['c']],
                   'd':[['h']],
                   'g':[['a','b','c']],
                   'f':[['h','b']]},
            'askables':['c','e']}


    print(top_down(['g'],kb))

    print(botton_up(kb))