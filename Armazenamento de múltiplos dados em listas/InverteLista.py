#Inverte a lista. Faça uma função que recebe uma lista e retorna essa mesma lista invertida.

def inverte_lista(l):
    l2=[]
    for k in l:
        l2.insert(0,k)
    return l2
