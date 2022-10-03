import numpy as np
import math
import copy
import matplotlib.pyplot as plt

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

    c_vals = []
    best_val = objective(sol)
    it = 0
    while it <= maxit:
        n = get_neighbor(sol)
        n_val = objective(n)
        if  n_val <= best_val:
            sol = copy.copy(n)
            c_val = n_val
            best_val = n_val 
        
        print(f'{it} : {best_val}')

        it +=1

        c_vals.append(c_val)

    return sol, best_val, c_vals

def simmulated_annealing(sol, objective, get_neighbor, maxit = 50):

    c_vals = []

    T = 100

    best_sol = copy.copy(sol)
    best_val = objective(sol)

    c_val = objective(sol)
    it = 0
    while it <= maxit:
        n = get_neighbor(sol)
        n_val = objective(n)

        if n_val <= best_val:
            best_val = n_val
            best_sol = copy.copy(n)

        if n_val <= c_val or np.random.rand() < math.exp(-(n_val-c_val)/T):
            sol = copy.copy(n)
            c_val = n_val
        
        c_vals.append(c_val)
        
        print(f'{it} : {best_val}')

        it +=1
        T = 0.99*T

    return best_sol, best_val , c_vals

if __name__ == '__main__':

    sol = list(range(100))

    sol1, val1, c_ls1 = local_search(sol, obj, swap, maxit = 10000)

    sol2, val2, c_ls2 = simmulated_annealing(sol, obj, swap, maxit = 10000)

    plt.plot(c_ls1)
    plt.plot(c_ls2)

    plt.show()