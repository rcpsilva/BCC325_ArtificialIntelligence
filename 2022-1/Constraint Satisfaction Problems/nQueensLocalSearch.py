import numpy as np
import copy

def different_column_violations(sol):

    conflicts = 0

    for i in range(len(sol)):
        for j in range(len(sol)):
            if (i!=j) and (sol[i]==sol[j]):
                conflicts += 1

    return conflicts

def different_diagonal_violations(sol):

    conflicts = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            deltay = abs(sol[i]-sol[j])
            deltax = abs(i - j)
            if (deltay == deltax):
                conflicts +=1

    return conflicts

def obj(sol):
    return different_diagonal_violations(sol) + different_column_violations(sol)

def rand_in_rand_position(sol):

    neighbor = copy.copy(sol)

    idx = np.random.randint(0,len(sol))
    value = np.random.randint(0,len(sol))

    neighbor[idx] = value

    return neighbor

def swap(sol):

    neighbor = copy.copy(sol)

    idx1 = np.random.randint(0,len(sol))
    idx2 = np.random.randint(0,len(sol))

    neighbor[idx1], neighbor[idx2] =  neighbor[idx2], neighbor[idx1] 

    return neighbor


def local_search(sol, objective, get_neighbor, maxit = 50):

    best_val = objective(sol)
    it = 0
    while it <= maxit:
        n = get_neighbor(sol)
        n_val = objective(n)
        if  n_val < best_val:
            sol = n
            best_val = n_val 
        
        print(f'{it} : {best_val}')

        it +=1

    return sol, best_val

if __name__ == '__main__':

    sol = [0,1,2,3,4,5,6,7]

    sol, val = local_search(sol, obj, swap, maxit = 100)

    print(sol)
    print(val)