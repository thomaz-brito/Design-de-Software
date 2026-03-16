#Desenvolva em Python uma função que recebe como argumento o número de elementos que serão usados na série e retorna o valor estimado de pi baseado no produto de Wallis.

import math as m
def pi_wallis(n):
    i=1
    soma=1
    if n%2==0:
        while i<=int(n/2):
            an=2*i
            bn=2*i+1
            soma=soma*(an/bn)**2
            i+=1
    else:
        while i<=m.ceil(n/2):
            an=2*i
            bn=2*i+1
            soma=soma*(an/bn)**2
            i+=1
        soma=soma/(an/bn)
    bn=2*(i-1)+1
    soma=soma*bn
    return 2*soma
