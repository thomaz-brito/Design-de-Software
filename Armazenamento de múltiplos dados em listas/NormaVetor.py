#Escreva uma função que recebe um vetor de dimensão arbitrária representado por uma lista e devolve a sua norma.

import math as m
def calcula_norma(x):
    soma=0
    for k in x:
        soma+=k**2
    norma=m.sqrt(soma)
    return norma
