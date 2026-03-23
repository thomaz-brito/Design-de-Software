#Faça uma função que recebe uma lista de números reais e retorna a soma de seus valores.


def soma_valores(n):
    i=0
    soma=0
    while i<len(n):
        soma=soma+n[i]
        i+=1
    return soma
