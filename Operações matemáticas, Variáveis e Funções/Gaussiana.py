#Faça uma função que recebe 3 números reais como argumento: x, mu e sigma. Essa função deve retornar o valor da fórmula da gaussiana:

import math
def calcula_gaussiana(x,mu,sigma):
    gaussiana=1/(sigma*math.sqrt(2*math.pi))*math.exp(-0.5*((x-mu)/sigma)**2)
    return gaussiana

