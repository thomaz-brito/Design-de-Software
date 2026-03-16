#Faça uma função que, dado um número inteiro qualquer maior do que 1, encontra seu maior fator primo.

def maior_fator_primo(n):
    i=2
    while i<=n and n!=1:
        if n%i==0:
            n=n/i
            if n!=1:
                i=2
        else:
            i+=1
    return i
