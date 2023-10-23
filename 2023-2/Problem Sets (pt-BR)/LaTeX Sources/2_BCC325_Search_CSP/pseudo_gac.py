GAC(<X,D,C>, {<X,c> | c in C and X in scope(c)}):

def GAC(<X,D,C>, to_do):
    while to_do:
        select and remove <X, c> from to_do
        let {Y1,....,Yk} = scope(c) \ {X}
        new_domain = {x|x in D(X) and exists y1 in D(Y1),...,yk in D(Yk)
                     such that c(X=x,Y1=y1,...Yk=yk)==True}
        if new_domain not equal D(X):
            to_do = to_do union {<Z,_c>| {X,Z} in scope(_c), _c!=c, Z!=X}
            D(X) = new_domain
    return D