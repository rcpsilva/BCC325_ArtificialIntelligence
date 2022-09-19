
def r0e7(sol,val):
    if len(sol) > 0:
        return sol[0] == 7

    return True

def different_column(sol,val):
    return not (val in sol)

def different_diagonal(sol,val):
    
    for i in range(len(sol)):
        deltay = abs(sol[i]-val)
        deltax = abs(i - len(sol))
        if (deltay == deltax):
            return False

    return True

def check_constraints(sol,val,constraints):

    for c in constraints:
        if not c(sol,val):
            return False

    return True


def search(domain, constraints, sol=[]):

    if len(sol) == len(domain):
        print(sol)
    else:
        for d in domain[len(sol)]:
            if check_constraints(sol, d, constraints):
                sol.append(d)
                search(domain,constraints,sol)
                sol.pop(-1)

if __name__ == '__main__':
    
    n = 8
    domain = [[i for i in range(n)] for j in range(n)]
    constraints = [different_column, different_diagonal,r0e7]
    
    print(domain)
    search(domain, constraints)