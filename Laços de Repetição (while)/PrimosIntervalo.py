#Escreva uma função que recebe dois números a e b e devolve a quantidade de números de primos p tais que a<=p<=b .


def primos_entre(a,b):
    k=a-1
    soma=0
    while k<b:
        i=2
        k+=1
        while i<k:
            if k%i!=0:
                i+=1
                if i==k:
                    soma+=1
            else:
                break
    if a==2:
        soma+=1
    return soma
