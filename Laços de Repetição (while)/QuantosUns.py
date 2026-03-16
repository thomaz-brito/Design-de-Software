#Escreva uma função que recebe um número inteiro e devolve a quantidade de vezes que o algarismo 1 ocorre nesse número.

def quantos_uns(n):
    soma=0
    n=abs(n)
    while n>=1:
        k=int(n%10)
        if k==1:
            soma+=1
        n=n/10
    return soma
