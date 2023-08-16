def bu(kb):
    c = []
    added_atom = True

    while added_atom:
        added_atom = False
        for head in kb:
            bodies = kb[head]
            for body in bodies:
                if not set(body).difference(set(c)):
                    if not head in c:
                        added_atom = True
                        c.append(head)
    return c


if __name__ == '__main__':

    kb = {'a':[['b','e'],['c']],
          'b':[['e']],
          'c':[[]]}

    print(bu(kb))