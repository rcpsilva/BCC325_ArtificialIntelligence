def is_valid_sk(s,ie,je,e):

    # Verifica linha
    for j in range(9):
        if s[ie][j] == e:
            return False


    # Verifica coluna
    for i in range(9):
        if s[i][je] == e:
            return False

    # Verifica regiao

    ir = ie//3 * 3
    jr = je//3 * 3

    for i in range(ir, ir+3):
        for j in range(jr, jr+3):
            if s[i][j] == e:
                return False
            
    return True

def is_complete(s):

    for row in s:
        for e in row:
            if e == 0:
                return False
    
    return True

def find_blank_square(s):
    for i in range(9):
        for j in range(9):
            if s[i][j] == 0:
                return (i,j)
    return ()

def backtrack_sk(s):

    if is_complete(s):
        print(s)
    else:
        blank  = find_blank_square(s)
        while blank:
            i,j = blank[0], blank[1]
            for e in range(1,10):
                if is_valid_sk(s,i,j,e):
                    s[i][j] = e
                    backtrack_sk(s)
                    s[i][j] = 0
            
            blank = find_blank_square(s)
                

def is_valid_nq(s,e):

    # Verifica se 'e' satisfaz as restrições para s

    # Verifica se temos rainhas na mesma coluna
    if e in s:
        return False
    
    # Verifica se existe outra rainha na mesma diagonal
    for i in range(len(s)):
        if abs(s[i] - e) == abs(len(s) - i):
            return False 
    
    return True

def backtrack_nq(s=[],n=8):

    if len(s) == n:
        print(s)
    else:
        for e in range(n):
            if is_valid_nq(s,e):
                s.append(e)
                backtrack_nq(s,n)
                s.pop(-1)

if __name__ == '__main__':

    #backtrack_nq([],4)

    s = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
    
    backtrack_sk(s)