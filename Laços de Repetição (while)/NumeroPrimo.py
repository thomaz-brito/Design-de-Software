#Faça uma função que recebe um número e retorna True caso ele seja primo ou False caso não.

def eh_primo(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:     
        i=2
        while i>=2 and i<x:
            resto=x%i
            if resto==0:
                return False
                i=x
            if i==(x-1):
                return True
            i+=1
