from sys import ps2
import numpy as np
import copy

def pop_init(k,n):
    return [np.random.permutation(n) for i in range(k)]

def mutation(sol):

    neighbor = copy.copy(sol)

    idx1 = np.random.randint(0,len(sol))
    idx2 = np.random.randint(0,len(sol))

    neighbor[idx1], neighbor[idx2] =  neighbor[idx2], neighbor[idx1] 

    return neighbor

def crossover(sol1,sol2):
    mask = np.random.randint(2, size=len(sol1))

    f1 = copy.copy(sol1)
    for i in range(len(sol1)):
        if mask[i] == 0:
            f1[i] = sol2[i]

    f2 = copy.copy(sol2)
    for i in range(len(sol2)):
        if mask[i] == 0:
            f2[i] = sol1[i]

    return f1,f2

def EA_nqueens(pop_size = 10, n = 8, gen_max= 1000):

    # Generate population
    pop = pop_init(pop_size,n)

    gen = 0 # Contador de gerações

    while gen < gen_max:

        for i in range(pop/2):
            # Seleção para reprodução
            idx_P1 = select_parent(pop)
            idx_P2 = select_parent(pop)
            # Crossover
            F1,F2 = crossover(pop[idx_P1],pop[idx_P2])
            # Mutação + atualização da população
            pop[idx_P1] = mutation(F1)
            pop[idx_P2] = mutation(F2)

        gen += 1

    # Encontrar o melhor indivíduo da população
    
    return best_ind

    

if __name__ == '__main__':

    pop = pop_init(10,8)
    for p in pop:
        print(p)

    print('------------------')
    print(pop[0])

    print(mutation(pop[0]))

    print('------------------')
    print(pop[0])
    print(pop[1])

    f1,f2 = crossover(pop[0],pop[1])

    print(f1)
    print(f2)


