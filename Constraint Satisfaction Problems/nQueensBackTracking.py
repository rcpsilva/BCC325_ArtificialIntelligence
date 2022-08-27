def check_nqueens(sol,value):

    diagonal = False
    for i in range(len(sol)):
        delta1 = abs(len(sol) - i)
        delta2 = abs(value - sol[i])
        diagonal = diagonal or (delta1 == delta2)

    return  not (value in sol) and not diagonal

def const(sol, value):
    return True if len(sol) == 0 else (sol[0]==7)
    
def check_constraints(sol,value,constraints):
    flag = True
    for c in constraints:
        flag = flag & c(sol,value)
    return flag

def search(domain, constraints, sol = []):

    if len(sol) == len(domain):
        print(sol)
    else:
        for value in domain[len(sol)]:
            if (check_constraints(sol,value, constraints)):
                sol.append(value)
                search(domain, constraints,sol)
                sol.pop(-1)
    
if __name__ == '__main__':
    
    n = 4
    domain = [[i for i in range(n)] for j in range(n)]
    #constraints = [check_nqueens, const]
    constraints = [check_nqueens]

    print(domain)
    search(domain, constraints)

