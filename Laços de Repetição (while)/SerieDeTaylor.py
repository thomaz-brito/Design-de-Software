#Pode-se usar uma série para calcular o valor do e (número de Euler ou Neperiano). 
#Basicamente, a ideia é somar uma sequência de números, e conforme se avança nesta sequência, mais perto se chega do valor desejado. 
#Para isso, leve em conta a série de Taylor para calcular e^x:
#Faça uma função em Python que recebe o valor x e o tamanho n da série e retorna e^x.

import math as m
def calcula_euler(x,n):
    i=0
    soma=0
    while i<=(n-1):
        valor=x**i/m.factorial(i)
        i=i+1
        soma = soma+valor
    return soma 
