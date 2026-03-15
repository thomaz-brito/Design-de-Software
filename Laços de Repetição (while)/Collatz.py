#Faça um programa que recebe um número inteiro n e determina qual número positivo inicial menor ou igual a n que gera a sequência de Collatz mais longa. Seu programa deve imprimir esse número.

n=int(input())
i=1
maior=0
if n==1:
    print(n)
else:
    while i<=n:
        a=i
        b=0
        while a!=1:
            if a%2==0:
                a=a/2
                b+=1
            else:
                a=3*a+1
                b+=1
        if b>maior:
            maior=b
            numero=i
        i+=1
    print(numero) 
