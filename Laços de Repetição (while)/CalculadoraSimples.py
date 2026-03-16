#Para isso, faça um programa que peça entradas para o usuário. A ordem das entradas do usuário será sempre um número e um operador e outro número (Não é necessário fazer nenhum tipo de validação). 
#Caso o usuário queira, ele pode continuar a sequência um operador e outro número.
#Quando o usuário digitar =, o programa deve parar de pedir entradas para o usuário e imprimir o resultado final no terminal.

n=int(input())
op=input()
res=n
while op!="=":
    n2=int(input())
    if op=="+":
        res=res+n2
    if op=="-":
        res=res-n2
    if op=="*":
        res=res*n2
    if op=="/":
        res=res/n2
    op=input()
print (res)
