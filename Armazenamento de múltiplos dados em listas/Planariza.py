#Faça uma função que recebe uma lista de listas e retorna uma lista simples composta por todos os elementos das listas originais.

def junta_listas(a):
    l=[]
    for k in a:
        for x in k:
            l.append(x)
    return l
