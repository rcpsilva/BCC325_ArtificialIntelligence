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


