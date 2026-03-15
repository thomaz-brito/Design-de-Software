#O valor de  pode ser aproximado a partir de uma série infinita
#Faça uma função chamada aproxima que recebe o valor de n e retorna o resultado da série utilizando os n termos.

def aproxima(n):
    k=1
    soma=0
    while k<=n:
        ak=1+(k-1)*2
        qk=(-1)**(k-1)*3**(k-1)
        termo = 1/(ak*qk)
        soma=soma+termo
        k+=1
    pi=12**(0.5)*(soma)
    return pi
