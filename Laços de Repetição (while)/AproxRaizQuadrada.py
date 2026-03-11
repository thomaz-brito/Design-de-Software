#Faça uma função que recebe um número inteiro n e devolve o número inteiro mais próximo da sua raiz quadrada. 
#Para isso você deve testar todos os números inteiros i a partir de 1 até que i elevado ao quadrado seja maior ou igual a n. 
#A resposta será i-1 ou i. Dentre as duas opções, devolva o valor cujo quadrado seja mais próximo de n.


import math
def aproxima_raiz(n):
    i=1
    while i**2<=n:
        i+=1
    if abs(i**2-n) > abs((i-1)**2-n):
        return (i-1)
    else:
        return i
