#A sequência de Fibonacci é uma sequência numérica que começa em 0 e 1 e então, a partir do terceiro elemento, cada número é dado pela soma dos dois números anteriores.
#Por exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
#Faça uma função que recebe uma lista de números e determina se essa lista obedece o padrão de uma sequência de Fibonacci ou não, retornando respectivamente: True ou False.

def eh_fibonacci(lista):
    soma=0
    if len(lista)<3:
        return False 
    else:
        for i in range (2,len(lista),1):
            if lista[i]!=lista[i-1]+lista[i-2]:
                soma+=1
        if soma==0:
            return True
        else:
            return False  
